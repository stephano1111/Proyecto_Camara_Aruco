import bluetooth
import time

def scan():
    print("\n Scnng Bluetooth devices")
    devices = bluetooth.discover_devices(lookup_names= True, lookup_class= True)
    number_of_devices = len(devices)
    print(number_of_devices, " devices found")

    for addr, name, devices_class in devices:
        print("\n Device: ")
        print("Device Name: %s " % (name))
        print("Device MAC address: %s " % (addr))
        print("\n")
        print("Device Class: %s " % (devices_class))
        print("\n")

    return
 
def connect (ubi):
    bd_addr = "00:18:E4:35:0F:D7"
    port = 1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    time.sleep(2)
    sock.send(ubi)
    sock.close()

connect()