import random
import time

from paho.mqtt import client as mqtt_client

MQTT_DEBUG_MODE = True

broker = '192.168.0.101'
port = 1883

client_id = 'raspberry-pi'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, topic, msg):
    result = client.publish(topic, str(msg))
    
    if MQTT_DEBUG_MODE:
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


def publish_loop(client):

    x = 0
    y = 0

    while True:
        time.sleep(0.1)

        xo = x
        yo = y
        x += random.random()/100
        y += random.random()/100
        
        dx = x - xo
        dy = y - yo

        publish(client, "Camara/x", x)
        publish(client, "Camara/y", y)
        publish(client, "PID/dx", dx)
        publish(client, "PID/dy", dy)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish_loop(client)

if __name__ == '__main__':
    run()