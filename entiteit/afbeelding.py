import random
import os

class Afbeelding:
    def __init__(self, assets_path="assets"):
        self._assets_path = assets_path
        self._afbeeldingen = [
            os.path.join(self._assets_path, file)
            for file in os.listdir(self._assets_path)
            if file.endswith(".png")
        ]

    def kies(self):
        return random.choices(self._afbeeldingen, k = 1)[0]