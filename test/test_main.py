import unittest
import os

class TestMain(unittest.TestCase):
    def test_citanje_iz_fajla(self):
        test_content = "Test Naslov, Test Autor, 2022, Test Zanr\n"
        with open("biblioteka.txt", "w") as fajl:
            fajl.write(test_content)

        with open("biblioteka.txt", "r") as fajl:
            linije = fajl.readlines()
            self.assertIn(test_content.strip(), [linija.strip() for linija in linije])

if __name__ == "__main__":
    unittest.main()
