class Biblioteka:
    def __init__(self):
        self.knjige = []

    def dodaj_knjigu(self, knjiga):
        self.knjige.append(knjiga)

    def prikazi_knjige(self):
        for knjiga u self.knjige:
            print(knjiga.prikazi_info())

    def pretrazi_knjige(self, kriterijum, kljucna_rec):
        rezultati = []
        with open("biblioteka.txt", "r") as fajl:
            for linija in fajl:
                podaci_knjige = linija.strip().split(", ")
                if kriterijum.lower() == "naslov" and kljucna_rec.lower() in podaci_knjige[0].lower():
                    rezultati.append(podaci_knjige)
                elif kriterijum.lower() == "autor" and kljucna_rec.lower() in podaci_knjige[1].lower():
                    rezultati.append(podaci_knjige)
                elif kriterijum.lower() == "godina" and kljucna_rec == podaci_knjige[2]:
                    rezultati.append(podaci_knjige)
                elif kriterijum.lower() == "zanr" and kljucna_rec.lower() in podaci_knjige[3].lower():
                    rezultati.append(podaci_knjige)
        return rezultati
