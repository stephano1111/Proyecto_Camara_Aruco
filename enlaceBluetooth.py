import bluetooth
import time

def scan():
    print("\n Scnng Bluetooth devices")
    devices = bluetooth.discover_devices(lookup_names= True, lookup_class= True)
    number_of_devices = len(devices)
    print(number_of_devices, " devices found")

    for addr, name, devices_class in devices:
        #if(name == "HC-05"):
        print("\n Device: ")
        print("Device Name: %s " % (name))
        print("Device MAC address: %s " % (addr))
        print("\n")
        print("Device Class: %s " % (devices_class))
        print("\n")

    return
 
def connect ():
   #98:D3:31:F5:8C:3E robot chiquito
    bd_addr = "00:18:E4:35:0F:D7"
    #bd_addr = "98:D3:31:F5:8C:3E"
    port = 1
    sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    #time.sleep(2)
    #Información para el robot
    sock.send('o')
    """
    time.sleep(1)
    sock.send("0")
    time.sleep(1)
    sock.send("0")
    sock.close()
    """
#scan()
connect()