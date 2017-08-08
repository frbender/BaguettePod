import serial
from array import array

"""
a class capable of communicating with an arduino aka pushing
bytes to the arduino and ensuring correct formatting
"""
class BPCommunication:
    def __init__(self, address = "/dev/tty.usbserial", baudrate = 2000000):
        self.connection = serial.Serial(address, baudrate)

    """
    sends an array of leds to the arduino
    (array in the form of [r, g, b] with r,g,b in [0, 255])
    """
    def transferBytes(self, data : [int]):
        # weave zeros into bytelist
        dataToSend = [255,255,255,255]
        i = 0
        for b in data:
            if i % 3 == 0:
                dataToSend += [0]
            dataToSend += [b]
            i += 1

        # convert int array to bytes
        dataAsBytes = array('B', dataToSend).tobytes()
        self.connection.write(dataAsBytes)

    def close(self):
        self.connection.close()
