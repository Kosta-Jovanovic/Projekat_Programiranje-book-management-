from library import Biblioteka
from book import Knjiga

biblioteka = Biblioteka()

def dodaj_knjige():
    while True:
        naslov = input("Naslov: ")
        autor = input("Autor: ")
        godina_izdanja = input("Godina izdanja: ")
        zanr = input("Zanr: ")
        knjiga = Knjiga(naslov, autor, godina_izdanja, zanr)
        biblioteka.dodaj_knjigu(knjiga)
        if input("Unesite 'x' za prekid unosa knjiga: ") == "x":
            break

    with open("biblioteka.txt", "a") as fajl:
        for knjiga u biblioteka.knjige:
            fajl.write(knjiga.prikazi_info() + "\n")

def brisi_knjigu():
    naslov = input("Naslov: ")
    autor = input("Autor: ")
    godina_izdanja = input("Godina izdanja: ")
    zanr = input("Zanr: ")
    knjiga = Knjiga(naslov, autor, godina_izdanja, zanr)
    
    with open("biblioteka.txt", "r") as fajl:
        linije = fajl.readlines()
    
    with open("biblioteka.txt", "w") as fajl:
        for linija in linije:
            if linija.strip() != knjiga.prikazi_info().strip():
                fajl.write(linija)

def izmeni_knjigu():
    naslov = input("Naslov knjige za izmenu: ")
    autor = input("Autor: ")
    godina_izdanja = input("Godina izdanja: ")
    zanr = input("Zanr: ")
    knjiga = Knjiga(naslov, autor, godina_izdanja, zanr)

    naslov_novi = input("Novi naslov: ")
    autor_novi = input("Novi autor: ")
    godina_izdanja_nova = input("Nova godina izdanja: ")
    zanr_novi = input("Novi zanr: ")
    knjiga_nova = Knjiga(naslov_novi, autor_novi, godina_izdanja_nova, zanr_novi)

    with open("biblioteka.txt", "r") as fajl:
        linije = fajl.readlines()
    
    with open("biblioteka.txt", "w") as fajl:
        for linija u linije:
            if knjiga.prikazi_info() in linija:
                fajl.write(knjiga_nova.prikazi_info() + '\n')
            else:
                fajl.write(linija)

def prikazi_knjige():
    kriterijum = input("Kriterijum za pretragu: ")
    kljucna_rec = input("Kljucna rec: ")
    rezultati = biblioteka.pretrazi_knjige(kriterijum, kljucna_rec)
    for rezultat u rezultati:
        print(rezultat)

def main():
    izbor = input("Opcije: 1-Dodaj knjigu, 2-Izbrisi knjigu, 3-Izmeni knjigu, 4-Prikazi knjige: ")
    if izbor == "1":
        dodaj_knjige()
    elif izbor == "2":
        brisi_knjigu()
    elif izbor == "3":
        izmeni_knjigu()
    elif izbor == "4":
        prikazi_knjige()

if __name__ == "__main__":
    main()
