import json
import paho.mqtt.client as mqtt
from pydantic import BaseModel, ValidationError

# Configuración idéntica de red
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_TELEMETRIA = "unmsm/fisi/smat/estaciones/1/lecturas"
LOG_FILE = "log_errores.txt"

# Esquema de Pydantic para garantizar la integridad técnica (Exigencia de la guía)
class LecturaSensorSchema(BaseModel):
    estacion_id: int
    valor: float  # Esto forzará a que si viene un texto no numérico, falle de inmediato
    timestamp: float

# Callback cuando nos conectamos con el Broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conectado exitosamente al Broker MQTT ({BROKER})")
        # Nos suscribimos al tópico con QoS 1
        client.subscribe(TOPIC_TELEMETRIA, qos=1)
        print(f"Suscrito al canal: {TOPIC_TELEMETRIA}")
    else:
        print(f"Error de conexión. Código de retorno: {rc}")

# Callback cuando llega un mensaje al canal suscrito
def on_message(client, userdata, msg):
    payload_str = msg.payload.decode("utf-8")
    print(f"\n[Mensaje Recibido] -> {payload_str}")
    
    try:
        # Intentamos parsear a JSON y validar con Pydantic
        datos_json = json.loads(payload_str)
        lectura_validada = LecturaSensorSchema(**datos_json)
        
        # Si pasa la validación con éxito, procesamos el negocio
        print(f"✓ [DATO VÁLIDO]: Estación {lectura_validada.estacion_id} reporta {lectura_validada.valor}°C/m.")
        
    except (json.JSONDecodeError, ValidationError) as e:
        # Requisito crítico de la guía: Atrapar el error sin que muera el programa
        # y guardarlo en log_errores.txt
        error_msg = f"[ERROR DE INTEGRIDAD / CORRUPCIÓN] Payload: {payload_str} | Detalle: {str(e)}\n"
        print(f"✗ {error_msg}")
        
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(error_msg)

def iniciar_suscriptor():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(BROKER, PORT, 60)
    
    print("--- Suscriptor MQTT de Alerta Temprana en escucha permanente ---")
    # loop_forever mantiene el hilo principal bloqueado escuchando los eventos de red de forma óptima
    client.loop_forever()

if __name__ == "__main__":
    iniciar_suscriptor()