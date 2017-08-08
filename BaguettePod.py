from BPCommunication import BPCommunication
from BPLedStrip import BPLedStrip
from BPAnimator import BPAnimator
from BPNightRiderAnimator import BPNightRiderAnimator

from threading import Timer


communicator = BPCommunication(address="/dev/cu.usbmodem1421")
animator = BPNightRiderAnimator()
leds = BPLedStrip(communicator, animator)

frame = 0

def update():
    global frame
    # Update Animation
    animator.update()
    # Send to Arduino
    leds.update()
    Timer(0.01, update).start()

if __name__ == "__main__":
    print("BaguettePod 1.0")
    ud = Timer(1.0, update)
    ud.start()
    print("Running...")

