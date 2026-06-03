import time
import json
import random
import paho.mqtt.client as mqtt

# Configuración del Broker y el Topic de la UNMSM
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_TELEMETRIA = "unmsm/fisi/smat/estaciones/1/lecturas"

def conectar_mqtt():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    return client

def simular_sensor():
    cliente = conectar_mqtt()
    cliente.loop_start()
    
    print("--- Publicador MQTT del SMAT Iniciado ---")
    try:
        while True:
            # Simulamos datos del sensor
            # De vez en cuando inyectamos un dato corrupto (un string en lugar de float) 
            # para probar la robustez del suscriptor exigida en la guía
            if random.random() < 0.15:
                valor_lectura = "CORRUPTO_ERROR" # Provocará falla de validación
            else:
                valor_lectura = round(random.uniform(10.0, 35.0), 2)
            
            payload = {
                "estacion_id": 1,
                "valor": valor_lectura,
                "timestamp": time.time()
            }
            
            mensaje_json = json.dumps(payload)
            # Publicamos con QoS 1 (Asegura al menos una entrega)
            cliente.publish(TOPIC_TELEMETRIA, mensaje_json, qos=1)
            print(f"[Sensor] Publicado en {TOPIC_TELEMETRIA}: {mensaje_json}")
            
            time.sleep(3) # Envía datos cada 3 segundos
    except KeyboardInterrupt:
        print("\nDeteniendo publicador...")
    finally:
        cliente.loop_stop()
        cliente.disconnect()

if __name__ == "__main__":
    simular_sensor()