class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja, zanr):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        self.zanr = zanr

    def prikazi_info(self):
        return f'{self.naslov}, {self.autor}, {self.godina_izdanja}, {self.zanr}'
