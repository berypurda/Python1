import feladat
import unittest

class TestHarcos(unittest.TestCase):
    def setUp(self):
        self.Anakin = feladat.Jedi("Anakin Skywalker", 5, 4)
        self.Vader = self.Anakin
        self.Windu = feladat.Jedi("Mace Windu", 11, 11)
        self.Yoda = feladat.Jedi("Yoda", 700, 10)
        self.Maul = feladat.Sith("Maul", 8, 8)
        self.Ahsoka = feladat.SemlegesHarcos("Ahsoka Tano", 9, 9, 9)
        self.Ventris = feladat.SemlegesHarcos("Ventris", 7, 5, 9)
        self.ObiWan = feladat.SemlegesHarcos("Obi-Wan Kenobi", 10, 10, 1)
        
    def test_harcos_pontszam(self):
        self.assertEqual(self.Anakin.pontszam, 20, "Nem megfelelő a Jedi pontszám kiszámolása")
        self.assertEqual(self.Maul.pontszam, 64, "Nem megfelelő a Sith pontszám kiszámolása")
        self.assertEqual(self.Ahsoka.pontszam, 81, "Nem megfelelő a Semleges pontszám kiszámolása (Egyenlő harag és egyensúly esetén)")
        self.assertEqual(self.Ventris.pontszam, 63, "Nem megfelelő a Semleges pontszám kiszámolása (Több harag esetén)")
        self.assertEqual(self.ObiWan.pontszam, 100, "Nem megfelelő a Semleges pontszámgvf kiszámolása (Több egyensúly esetén)")
    
    def test_harcos_fenykardszin(self):
        self.assertEqual(self.Anakin.fenykardszin, "kék", "Nem megfelelő a Jedi kék fénykard szín")
        self.assertEqual(self.Windu.fenykardszin, "lila", "Nem megfelelő a Jedi lila fénykard szín")
        self.assertEqual(self.Yoda.fenykardszin, "zöld", "Nem megfelelő a Jedi zöld fénykard szín")
        self.assertEqual(self.Maul.fenykardszin, "piros", "Nem megfelelő a Sith piros fénykard szín")
        self.assertEqual(self.Ahsoka.fenykardszin, "fehér", "Nem megfelelő a Semleges fehér fénykard szín")
        self.assertEqual(self.Ventris.fenykardszin, "piros", "Nem megfelelő a Semleges piros fénykard szín")
        self.assertEqual(self.ObiWan.fenykardszin, "kék", "Nem megfelelő a Semleges kék fénykard szín")
    
    def test_harcos_tapasztalat(self):
        self.assertEqual(self.Anakin.tapasztalat, 5, "Nem megfelelő a Jedi tapasztalat")
        self.assertEqual(self.Maul.tapasztalat, 8, "Nem megfelelő a Sith tapasztalat")
        self.assertEqual(self.Ahsoka.tapasztalat, 9, "Nem megfelelő a Semleges tapasztalat")
        
    def test_harcos_egyensuly(self):
        self.assertEqual(self.Anakin.egyensuly, 4, "Nem megfelelő a Jedi egyensúly")
        self.assertEqual(self.Ahsoka.egyensuly, 9, "Nem megfelelő a Semleges egyensúly")
    
    def test_harcos_harag(self):
        self.assertEqual(self.Ahsoka.harag, 9, "Nem megfelelő a Semleges harag")
        self.assertEqual(self.Maul.harag, 8, "Nem megfelelő a Sith harag")
        
    def test_harcos_nev(self):
        self.assertEqual(self.Anakin.nev, "Anakin Skywalker", "Nem megfelelő a Jedi neve")
        self.assertEqual(self.Ahsoka.nev, "Ahsoka Tano", "Nem megfelelő a Semleges neve")
        self.assertEqual(self.Maul.nev, "Darth Maul", "Nem megfelelő a Sith neve")
        
    def test_harc(self):
        self.assertEqual(self.Anakin.harcol(self.Maul), "Darth Maul nyerte a harcot " + self.Maul.fenykardszin + " fénykarddal", "Nem megfelelő a harc, (You don't have the highground)")
        self.assertEqual(self.Anakin.harcol(self.Vader), "Elmenekültek", "Nem megfelelő a harc, (You don't have the highground)")