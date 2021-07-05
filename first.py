import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully !!")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

# create the client111
client = mqtt.Client()
client.on_connect = on_connect  # here on_connect is attribut of acknowledement from sever about connection that return rc value
client.on_publish = on_publish

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("ishan", "First111")

# connect to HiveMQ Cloud on port 8883
client.connect("45c9a8b593d443128be71ca023af4b1e.s1.eu.hivemq.cloud", 8883)

# subscribe to the topic

# publish "Hello" to the topic "my/test/topic"
client.publish("testtopic/sensordata", "28 degree C")

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()