"""
provides animation behavior
"""
class BPAnimator:
    def __init__(self, numLeds = 60):
        self.numLeds = numLeds

    """
    calculates next frame
    """
    def update(self):
        return

    """
    calculates the color at a given led
    """
    def getColorAtLed(self, ledPos):
        # check if led is in range
        if ledPos < 0 or ledPos >= self.numLeds:
            print("ledPos too big or too small")
            return

        return [0, 0, 0]