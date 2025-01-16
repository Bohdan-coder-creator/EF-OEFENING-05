from entiteit.afbeelding import Afbeelding

class SlotMachine:
    def __init__(self):
        self._aantal = 0
        self._score = 0
        self._punten = 0
        self._afbeelding = Afbeelding()
        self._afbeeldingen = []

    def spin(self):
        self._aantal += 1
        self._afbeeldingen = [self._afbeelding.kies() for _ in range(3)]

        unique_images = len(set(self._afbeeldingen))
        if unique_images == 3:
            self._punten = 0
        elif unique_images == 2:
            self._punten = 1
        else:
            self._punten = 3

        self._score += self._punten

    def afbeeldingen(self):
        return self._afbeeldingen

    def punten(self):
        return self._punten

    def score(self):
        return self._score

    def aantal(self):
        return self._aantal
