from random import randint

class KopOfMunt:
    def __init__(self):
        self._geschiedenis = []

    def werp(self):
        worp = 'kop' if randint(0, 10000) % 2 == 0 else 'munt'
        self._geschiedenis.append(worp)
        return worp
    
    def geschiedenis(self):
        return self._geschiedenis