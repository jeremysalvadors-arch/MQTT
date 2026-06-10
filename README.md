1. ¿Por qué HTTP REST no es adecuado para 10,000 sensores industriales?

Utilizar HTTP REST para conectar 10,000 sensores que envían datos cada 100 milisegundos no resulta práctico porque genera una gran carga tanto en la red como en el servidor.
Por un lado, se producirían alrededor de 100,000 solicitudes por segundo. Cada petición HTTP incluye cabeceras relativamente grandes en comparación con los datos enviados por los sensores, lo que ocasiona un uso excesivo del ancho de banda debido a información repetitiva.
Por otro lado, HTTP funciona bajo un modelo de solicitud-respuesta, por lo que el servidor debe gestionar una enorme cantidad de conexiones simultáneas. Esto incrementa el consumo de memoria y CPU, pudiendo afectar seriamente el rendimiento del sistema.
En contraste, MQTT utiliza cabeceras muy pequeñas, mantiene conexiones persistentes y trabaja mediante un modelo de publicación/suscripción, lo que permite manejar grandes volúmenes de mensajes con un consumo mucho menor de recursos.

2. ¿Cuándo es necesario usar QoS 2 en MQTT?

QoS 2 garantiza que un mensaje se entregue exactamente una vez, evitando pérdidas o duplicaciones. Su uso es indispensable cuando un mensaje repetido puede causar problemas graves.

Algunos ejemplos son:

Transacciones financieras, donde un mensaje duplicado podría generar cobros dobles.
Control de maquinaria industrial, donde repetir una orden puede provocar fallos o accidentes.
Gestión automatizada de inventarios, evitando registros incorrectos de stock.
Sistemas médicos críticos, donde la duplicación de eventos puede afectar decisiones clínicas.

En cambio, QoS 0 es suficiente para datos de monitoreo frecuentes, como lecturas de temperatura, donde la pérdida ocasional de un mensaje no tiene consecuencias importantes.

3. MQTT y la sostenibilidad tecnológica en zonas rurales

El uso de protocolos eficientes como MQTT contribuye a la sostenibilidad tecnológica al reducir el consumo de recursos y energía.
Al transmitir menos datos que HTTP, disminuye la carga de procesamiento en servidores y centros de datos, ayudando a reducir el consumo eléctrico y las emisiones de carbono.
Además, en comunidades rurales donde los dispositivos funcionan con baterías o energía solar, MQTT permite comunicaciones más rápidas y eficientes, prolongando la vida útil de los equipos.
Finalmente, su bajo consumo de ancho de banda facilita la implementación de soluciones IoT en zonas con conectividad limitada o costosa, promoviendo una mayor inclusión tecnológica y acceso a herramientas de monitoreo y desarrollo.
