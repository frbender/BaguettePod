from BPAnimator import BPAnimator
from BPCommunication import BPCommunication

"""
represents a led strip of variable length
"""
class BPLedStrip:
    def __init__(self, communication : BPCommunication, animator : BPAnimator, numLeds = 60):
        self.communication = communication
        self.animation = animator
        self.numLeds = numLeds
        self.leds = [[0, 0, 0] for _ in range(numLeds)]

    """
    updates the strip using the animator and
    communicator specified in the constructor
    """
    def update(self):
        for i in range(self.numLeds):
            self.leds[i] = self.animation.getColorAtLed(i)
        self.communication.transferBytes([c for led in self.leds for c in led])