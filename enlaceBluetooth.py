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

