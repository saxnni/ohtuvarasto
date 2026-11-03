import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-10, -10)
        self.varasto3 = Varasto(10, 20)
        self.varasto4 = Varasto(10)
        self.varasto5 = Varasto(0)

    def test_nollaa_virheellinen_tilavuus(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_nollaa_virheellinen_saldo(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_saldo_taynna(self):
        self.assertAlmostEqual(self.varasto2.saldo, self.varasto2.tilavuus)

    def test_virheellinen_lisaus(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ei_lisata_liikaa(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_virheellinen_otto(self):
        self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_saldo_info(self):
        self.assertEqual(str(self.varasto5), f"saldo = 0, vielä tilaa 0.0")

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
