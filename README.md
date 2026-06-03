1 ¿Por qué no es viable utilizar una arquitectura síncrona HTTP REST para interconectar 10,000 sensores industriales que reportan datos cada 100 milisegundos?
Utilizar una arquitectura síncrona HTTP REST para este escenario es inviable debido a la sobrecarga de paquetes. HTTP arrastra consigo cabeceras de texto de aproximadamente 500 bytes; mientas que, con MQTT, como su cabecera fija es de apenas 2 bytes.
Explique en qué escenarios de desarrollo de software es imperativo utilizar el nivel QoS 2 en lugar de QoS 0.
El nivel QoS 2 es obligatorio en escenarios donde la pérdida de datos es inaceptable y la duplicación de los mismos puede ser perjudicial. Escenarios como: Sistemas de transacciones financieras y facturación, sistemas de control o sistemas de telomedicina.
¿Cómo contribuye el diseño de protocolos eficientes como MQTT a la sostenibilidad tecnológica de las regiones rurales del Perú?
