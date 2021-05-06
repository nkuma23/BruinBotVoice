# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2
# Imports
import serial



def sendMessage(message):
    try:
        usb = serial.Serial(USB_PORT, 9600, timeout=2)
    except:
        print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
        print("Exiting program.")
        return -1
    usb.write(bytes(message, 'ascii'))

