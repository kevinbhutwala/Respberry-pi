import time
import sqlite3
import datetime
import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print(f"Received Message {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.hivemq.com",1883,60)

str = "Temp";

for i in range(7):
    client.publish(topic="bad",payload=str+" "+f"{i}",qos=0,retain=False)
    print(f"Hua {i}")
    time.sleep(3)
client.loop_forever()
