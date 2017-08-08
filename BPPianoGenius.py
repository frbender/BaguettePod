

class BPPianoGenius:
    def __init__(self, keyAmount = 88):
        #Key Aamount on keyboard
        self.keyAmount = keyAmount

        #Intialize Array of pressed keys with zeros
        self.pressedKeys = []
        for i in range(0, keyAmount):
            self.pressedKeys.append(0)

        #This Array contains all keys mapped to one octave
        self.moduloKeys = []
        for i in range(0, 12):
            self.moduloKeys.append(0)

        #Chordmap: maps tone distances from base key to specific chord
        self.chordmap = {
            "maj": [0, 4, 7], #Major
            "min": [0, 3, 7]  #Minor
        }

        return

    def refreshModuloKeys(self):
        for i in range(0, 12):
            self.moduloKeys[i] = 0

        for i in range(0, self.keyAmount):
            self.moduloKeys[i % 12] += self.pressedKeys[i]
        return



    def pressKey(self, index, velocity):
        self.pressedKeys[index] = velocity  
        self.refreshModuloKeys()
        return
        


    def releaseKey(self, index):
        self.pressedKeys[index] = 0
        self.refreshModuloKeys()
        return


    def isChordPlayed(self, baseKey, chord):
        for chordOffs in self.chordmap[chord]:
            if self.moduloKeys[(baseKey + chordOffs) % 12] == 0:
                    return False
        return True

    def getChord(self, baseKey):
        resultChord = "" #Will stay "" if no chord is found

        for chord in self.chordmap:
            if self.isChordPlayed(baseKey, chord):
                resultChord = chord

        return resultChord