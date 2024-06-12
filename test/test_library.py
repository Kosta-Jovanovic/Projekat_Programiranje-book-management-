from io import StringIO
import unittest
from library import Biblioteka
from book import Knjiga

class TestBiblioteka(unittest.TestCase):
    def test_dodaj_knjigu(self):
        knjiga = Knjiga("Test Naslov", "Test Autor", 2022, "Test Zanr")
        biblioteka = Biblioteka()
        biblioteka.dodaj_knjigu(knjiga)
        self.assertEqual(len(biblioteka.knjige), 1)

    def test_prikazi_knjige(self):
        knjiga = Knjiga("Test Naslov", "Test Autor", 2022, "Test Zanr")
        biblioteka = Biblioteka()
        biblioteka.dodaj_knjigu(knjiga)
        capture_output = StringIO()
        sys.stdout = capture_output
        biblioteka.prikazi_knjige()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture_output.getvalue().strip(), "Test Naslov, Test Autor, 2022, Test Zanr")

if __name__ == "__main__":
    unittest.main()
