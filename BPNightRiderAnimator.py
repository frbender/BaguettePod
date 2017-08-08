from BPAnimator import BPAnimator

class BPNightRiderAnimator(BPAnimator):
    def __init__(self, numLeds = 60):
        BPAnimator.__init__(self, numLeds)
        self.currentLed = 0
        self.up = True

    def update(self):
        if self.up:
            self.currentLed += 1
        else:
            self.currentLed -= 1
        if self.currentLed == self.numLeds or self.currentLed < 0:
            self.up = not self.up
            self.update()

    def getColorAtLed(self, ledPos):
        if ledPos == self.currentLed:
            return [255, 0, 0]
        else:
            return [0, 0, 0]
