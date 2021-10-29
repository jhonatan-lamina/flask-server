#IMPORTANT: Replace email, password and topics with your data

import paho.mqtt.client as mqtt
from time import sleep
from random import randint

def connected(client, userdata, flags, rc):
    print ("Connected to the result code: " + str (rc))
    #IMPORTANT: Replace email and topic1 with your data
    client.subscribe ("email/topic1")

def message (client, userdata, msg):
    #print (msg.topic + " " + str (msg.payload))
    print('New data received: '+msg.payload.decode('utf-8'))

client = mqtt.Client ()
#IMPORTANT: Replace email and password with your data
client.username_pw_set ('email', 'password')
client.on_connect = connected
client.on_message = message
client.connect ("maqiatto.com", 1883, 60)
sleep(3)

while 1:
    client.loop()
    data1 = randint(100,200)
    data2= randint(200,300)
    print('Sent: '+str(data1)+'|'+str(data2))
    #IMPORTANT: Replace email and topic2 with your data
    client.publish('email/topic2', str(data1)+'|'+str(data2))
    sleep(3)