class BPPianoGenius:
    def __init__(keyAmount = 88):
        #Key Aamount on keyboard
        self.keyAmount = keyAmount

        #Intialize Array of pressed keys with zeros
        self.pressedKeys = []
        for i in range(0, keyAmount):
            pressedKeys.append(0)


    def pressKey(index, velocity):
        pressedKeys[index] = velocity;
        
    def releaseKey(index):
        pressedKeys[index] = 0;


