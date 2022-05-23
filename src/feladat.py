from abc import ABC, abstractmethod

class Harcos(ABC):
    
    @property
    @abstractmethod
    def nev(self):
        pass

    @property
    @abstractmethod
    def tapasztalat(self):
        pass
    
    @property
    @abstractmethod
    def fenykardszin(self):
        pass
    
    @property
    @abstractmethod
    def pontszam(self):
        pass
    
    def harcol(self, Harcos):
        if(self.pontszam > Harcos.pontszam):
            return self.nev + " nyerte a harcot " + self.fenykardszin + " fénykarddal"
        elif(self.pontszam < Harcos.pontszam):
            return Harcos.nev + " nyerte a harcot " + Harcos.fenykardszin + " fénykarddal"
        else:
            return "Elmenekültek"
        
class Jedi(Harcos):
    def __init__(self, nev, tapasztalat, egyensuly):
        self._nev = nev
        self._tapasztalat = tapasztalat
        self.egyensuly = egyensuly
        
    @property
    def nev(self):
        return self._nev

    @property
    def tapasztalat(self):
        return self._tapasztalat
        
    @property
    def fenykardszin(self):
            if 5 < self.egyensuly <= 10:
                return "zöld"
            elif 1 <= self.egyensuly <= 5:
                return "kék"
            else:
                return "lila"
        
    @property
    def pontszam(self):
        return self.tapasztalat * self.egyensuly
        
class Sith(Harcos):
    def __init__(self, nev, tapasztalat, harag):
        self._nev = "Darth " + nev
        self._tapasztalat = tapasztalat
        self.harag = harag
            
            
    @property
    def nev(self):
        return self._nev

    @property
    def tapasztalat(self):
        return self._tapasztalat
    
    @property
    def fenykardszin(self):
            return "piros"
        
    @property
    def pontszam(self):
        return self.tapasztalat * self.harag
        
class SemlegesHarcos(Jedi, Sith):
    def __init__(self, nev, tapasztalat, egyensuly, harag):
        self._nev = nev
        self._tapasztalat = tapasztalat
        self.egyensuly = egyensuly
        self.harag = harag
        
    @property
    def nev(self):
        return self._nev

    @property
    def tapasztalat(self):
        return self._tapasztalat    
    
    @property
    def fenykardszin(self):
        if self.egyensuly > self.harag:
            return "kék"
        elif self.egyensuly < self.harag:
            return "piros"
        else:
            return "fehér"
        
    @property
    def pontszam(self):
        if self.egyensuly >= self.harag:
            return self.tapasztalat * self.egyensuly
        else:
            return self.tapasztalat * self.harag
