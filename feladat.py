from abc import ABC, abstractmethod


class Labbeli(ABC):

    @property
    @abstractmethod
    def viselheto(self):
        pass

    def menosegi_faktor(self):
        return 0


class Cipo(Labbeli):
    def __init__(self, marka, szin):
        self.marka = marka
        self.szin = szin
        self.kopottsag = 0

    @property
    def viselheto(self):
        if(self.kopottsag < 10):
            return True
        else:
            return False

    def menosegi_faktor(self):
        return (len(self.marka) + len(self.szin)) // 2

    def visel(self):
        self.kopottsag += 1


class Converse(Cipo):
    def __init__(self, szin):
        super().__init__(marka="Converse", szin=szin)

    def menosegi_faktor(self):
        return super().menosegi_faktor() + 5


class Csizma(Labbeli):
    def __init__(self, szar_magassag):
        self.szar_magassag = szar_magassag
        self.lyukas = False

    def hasznal(self, szam):
        if(szam > 100):
            self.lyukas = True

    @property
    def viselheto(self):
        return not self.lyukas


class HelloKittyCsizma(Cipo, Csizma):
    def __init__(self, szin):
        Cipo.__init__(self, marka="Hello Kitty csizma", szin=szin)
        Csizma.__init__(self, szar_magassag=25)

    @property
    def viselheto(self):
        return super().viselheto and not self.lyukas


# def main():
#     Cip = Cipo("nike", "fekete")
#     print(Cip.viselheto)
#     Csiz = Csizma(25)
#     Csiz.hasznal(125)
#     print(Csiz.viselheto)
#     Hel = HelloKittyCsizma("Fehér")

#     Hel.hasznal(125)

#     # for i in range(0, 20):
#     #     Hel.visel()

#     print(Hel.viselheto)


# if __name__ == "__main__":
#     main()
