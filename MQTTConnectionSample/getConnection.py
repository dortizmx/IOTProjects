# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time

broker_address = "m10.cloudmqtt.com"
broker_port = 12061
broker_user = "coto6g"
broker_password = "playadel"
rc = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("DEPTO211G/#",0)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print "Topic: ", str(msg.topic) + "\nMessage: " +str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(broker_user, broker_password)

client.connect(broker_address, broker_port)

#client.subscribe("DEPTO211G/ESTANCIA/#",0)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
