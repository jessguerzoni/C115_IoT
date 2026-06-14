import random
import time
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORTA = 1883

TOPICO = "incubadora/temperatura"

cliente = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="SIMULADOR_INCUBADORA"
)


cliente.connect(BROKER, PORTA)

cliente.loop_start()

print("Conectado!")
print()

while True:

    temperatura = round(
        random.uniform(34.0, 40.0),
        1
    )

    cliente.publish(
        TOPICO,
        str(temperatura)
    )

    print(
        f"Temperatura enviada: {temperatura} °C"
    )

    time.sleep(2)