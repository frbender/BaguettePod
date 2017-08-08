

class BPPianoGenius:
    def __init__(self, keyAmount = 88):
        #Key Aamount on keyboard
        self.keyAmount = keyAmount

        #Intialize Array of pressed keys with zeros
        self.pressedKeys = []
        for i in range(0, keyAmount):
            pressedKeys.append(0)

        #This Array contains all keys mapped to one octave
        self.moduloKeys = []
        for i in range(0, 12):
            pressedKeys.append(0)

        #Chordmap: maps tone distances from base key to specific chord
        self.chordmap = [
            [0, [0, 4, 7]], #0: Major
            [1, [0, 3, 7]]  #1: Minor
        ]

        return

    def refreshModuloKeys():
        for i in range(0, 12):
            pressedKeys[i] = 0

        for i in range(0, keyAmount):
            moduloKeys[i % 12] += pressedKeys[i]
        return



    def pressKey(index, velocity):
        pressedKeys[index] = velocity;
        
        return
        


    def releaseKey(index):
        pressedKeys[index] = 0;

        return


    def detectChord(baseKey):
        # for i in range(0, len(chordmap)):

        return