#Név: Járfás Tamás
#Szak: Mérnökinformatikus (távoktatás)
#Neptun-kód: A1I3JF

from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, agyasok_szama):
        self.szobaszam = szobaszam
        self.agyasok_szama = agyasok_szama

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 1)

    @property
    def ar(self):
        return 10000  # Egyágyas szoba ára

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 2)

    @property
    def ar(self):
        return 15000  # Kétágyas szoba ára

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class SzallodaRendszer:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.datum == datum:
                return "A szoba már foglalt ezen a napon!"
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum))
                return f"Sikeres foglalás a {datum}-i dátumra a {szobaszam}-es szoba számára {szoba.agyasok_szama} ággyal, ára: {szoba.ar} Ft."
        return "Nincs ilyen szoba a szállodában!"

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "Sikeres lemondás."
        return "Nincs ilyen foglalás."

    def listazas(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        foglalasok_listaja = "\n".join([f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}, Ár: {foglalas.szoba.ar} Ft" for foglalas in self.foglalasok])
        return f"A foglalások:\n{foglalasok_listaja}"

    def szobak_megtekintese(self):
        if not self.szalloda.szobak:
            return "Nincsenek szobák a szállodában."
        szobak_lista = "\n".join([f"Szoba: {szoba.szobaszam}, Ágyak száma: {szoba.agyasok_szama}" for szoba in self.szalloda.szobak])
        return f"A szálloda szobái és ágyainak száma:\n{szobak_lista}"

# Szálloda, szobák és foglalások létrehozása
szoba1 = EgyagyasSzoba("101")
szoba2 = KetagyasSzoba("201")
szoba3 = EgyagyasSzoba("301")

szalloda = Szalloda("Kiváló Szálloda")
szalloda.add_szoba(szoba1)
szalloda.add_szoba(szoba2)
szalloda.add_szoba(szoba3)

rendszerszalloda = SzallodaRendszer(szalloda)
rendszerszalloda.foglalas("101", datetime(2024, 4, 22))
rendszerszalloda.foglalas("201", datetime(2024, 4, 23))
rendszerszalloda.foglalas("301", datetime(2024, 4, 25))
rendszerszalloda.foglalas("101", datetime(2024, 4, 26))
rendszerszalloda.foglalas("201", datetime(2024, 4, 28))

# Felhasználói felület
while True:
    print("\nVálassz műveletet:")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Szobák és ágyak megtekintése")
    print("5. Kilépés")
    valasztas = input("Választás: ")

    if valasztas == "1":
        szobaszam = input("Add meg a foglalandó szoba számát: ")
        datum = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        datum = datetime.strptime(datum, "%Y-%m-%d")
        print(rendszerszalloda.foglalas(szobaszam, datum))
    elif valasztas == "2":
        szobaszam = input("Add meg a lemondani kívánt foglalás szoba számát: ")
        datum = input("Add meg a lemondani kívánt foglalás dátumát (YYYY-MM-DD formátumban): ")
        datum = datetime.strptime(datum, "%Y-%m-%d")
        print(rendszerszalloda.lemondas(szobaszam, datum))
    elif valasztas == "3":
        print(rendszerszalloda.listazas())
    elif valasztas == "4":
        print(rendszerszalloda.szobak_megtekintese())
    elif valasztas == "5":
        print("Kilépés...")
        break
    else:
        print("Érvénytelen választás!")
