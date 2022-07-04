from mqtt import MQTTClient
import time
import ujson
import machine
import config
from machine import Pin
from dht import DHT

def sub_cb(topic, msg):
   print(msg)

# The MQTT topics that we publish data to
temp_topic = config.TEMP_TOPIC
hum_topic = config.HUM_TOPIC

pin = 'P19' # marked with a 32 on the Heltec loRa 32 board because reasons
th = DHT(Pin(pin, mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)

# MQTT Setup
client = MQTTClient(config.SERIAL_NUMBER,
                    config.MQTT_BROKER,
                    user=config.TOKEN,
                    password=config.TOKEN,
                    port=config.PORT)
client.set_callback(sub_cb)
client.connect()
print('Connected to MQTT broker')

while True:
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()
    client.publish(topic=temp_topic, msg=str(result.temperature))
    client.publish(topic=hum_topic, msg=str(result.humidity))
    client.check_msg()

    time.sleep(300)
