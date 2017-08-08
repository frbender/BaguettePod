# Installing

1. Install pyserial:
pip install pyserial

read_spacers = 0
current_led
for byte b in buffer:
    if b == 0xFF:
        read_spacers += 1
    else:
        if read_spacers > 3:
            # found start of frame!
            readLeds()
        read_spacers = 0

readLeds():
    led_lesing()
