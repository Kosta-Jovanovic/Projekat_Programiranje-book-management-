import unittest
from book import Knjiga

class TestKnjiga(unittest.TestCase):
    def test_naslov(self):
        knjiga = Knjiga("Na Drini cuprija", "Ivo Andric", 1954, "Roman")
        self.assertEqual(knjiga.naslov, "Na Drini cuprija")

    def test_autor(self):
        knjiga = Knjiga("Na Drini cuprija", "Ivo Andric", 1954, "Roman")
        self.assertEqual(knjiga.autor, "Ivo Andric")

    def test_godina_izdanja(self):
        knjiga = Knjiga("Na Drini cuprija", "Ivo Andric", 1954, "Roman")
        self.assertEqual(knjiga.godina_izdanja, 1954)

    def test_zanr(self):
        knjiga = Knjiga("Na Drini cuprija", "Ivo Andric", 1954, "Roman")
        self.assertEqual(knjiga.zanr, "Roman")

    def test_prikazi_info(self):
        knjiga = Knjiga("Na Drini cuprija", "Ivo Andric", 1954, "Roman")
        self.assertEqual(knjiga.prikazi_info(), "Na Drini cuprija, Ivo Andric, 1954, Roman")

if __name__ == "__main__":
    unittest.main()
