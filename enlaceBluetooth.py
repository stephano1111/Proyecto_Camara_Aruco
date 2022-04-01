import bluetooth

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

def scan_services():

   print("Scanning for bluetooth devices: ")

   devices = bluetooth.discover_devices(lookup_names = True)

   number_of_devices = len(devices)

   print(number_of_devices, "devices found")

   for addr,name in devices:

      print("\n")

      print("Device Name: %s" % (name))

      print("Device MAC Address: %s" % (addr))

      print("Services Found:")

      services = bluetooth.find_service(address=addr)

      if len(services) <=0:

          print("zero services found on", addr)

      else:

          for serv in services:

              print(serv['name'])

      print("\n")

   return()

scan()
#scan_services()
"""
import serial
import keyboard as k


try:
    ser = serial.Serial("com3", 9600)

    while True:
        if k.is_pressed("y"):
            ser.write(b'y')
        elif k.is_pressed("n"):
            ser.write(b'n')
        if k.is_pressed("ENTER"):
            ser.close()
            break
        
except TimeoutError:
    print("error")
finally:
    print("done")
"""
