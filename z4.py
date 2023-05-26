class Samochod:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

    def podaj_zasieg(self):
        pass


class SamochodElektryczny(Samochod):
    def __init__(self, marka, model, rok_produkcji, pojemnosc_baterii):
        super().__init__(marka, model, rok_produkcji)
        self.pojemnosc_baterii = pojemnosc_baterii

    def podaj_zasieg(self):
        return self.pojemnosc_baterii * 5


class SamochodSpalinowy(Samochod):
    def __init__(self, marka, model, rok_produkcji, pojemnosc_zbiornika):
        super().__init__(marka, model, rok_produkcji)
        self.pojemnosc_zbiornika = pojemnosc_zbiornika

    def podaj_zasieg(self):
        return self.pojemnosc_zbiornika * 15


class SamochodHybrydowy(SamochodSpalinowy):
    def __init__(self, marka, model, rok_produkcji, pojemnosc_baterii, pojemnosc_zbiornika):
        super().__init__(marka, model, rok_produkcji, pojemnosc_zbiornika)
        self.pojemnosc_baterii=pojemnosc_baterii
    def podaj_zasieg(self):
        return self.pojemnosc_baterii*2 + self.pojemnosc_zbiornika*8


