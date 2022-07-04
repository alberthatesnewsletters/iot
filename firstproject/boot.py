import network
import time
import config

# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect(config.WIFI_SSID, auth=(network.WLAN.WPA2, config.WIFI_PASS))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())
