import network
import socket
from machine import Pin

# onboard LED on GPIO2
led = Pin(2, Pin.OUT)

# WiFi setup
SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass

print("Connected, IP:", wlan.ifconfig()[0])

# Start socket server
addr = socket.getaddrinfo("0.0.0.0", 8080)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Listening on", addr)

while True:
    cl, addr = s.accept()
    data = cl.recv(1024).decode().strip()
    print("Received:", data)

    if data == "ON":
        led.value(1)
    elif data == "OFF":
        led.value(0)

    cl.send("OK")
    cl.close()
