class Liczba:
    def __init__(self):
        self.liczba = []
        self.sumy = []
        self.liczba_operacji = []
        self.index: int = 0

    def print_f(self):
        for i in range(len(self.liczba)):  # Używamy długości listy
            print(f"{self.liczba[i]};{self.sumy[i]};{self.liczba_operacji[i]}")

    def convert_to_int(self):
        """Konwertuje listy stringów na listy liczb całkowitych."""
        try:
            self.liczba = [int(x) for x in self.liczba]
            self.sumy = [int(x) for x in self.sumy]
            self.liczba_operacji = [int(x) for x in self.liczba_operacji]
        except ValueError as e:
            print(f"Błąd konwersji: {e}")

    def filtr_list(self):
        """
            Przez to że w naszym programie w c stawiamy na wydajność nie dokładność część liczb może być obliczna wielokrotnie.
            Ta funkcja zajmie się odfiltrowywaniem odpowiednich elementów. A potem posortuje liste.
        """

        seen = set()  # Używamy zbioru do śledzenia już widzianych liczb
        indeksy_do_usuniecia = []

        for i, liczba in enumerate(self.liczba):
            if liczba in seen:
                indeksy_do_usuniecia.append(i)
            else:
                seen.add(liczba)

        # Usuwamy elementy na tych samych indeksach w trzech listach
        for indeks in reversed(indeksy_do_usuniecia):
            del self.liczba[indeks]
            del self.sumy[indeks]
            del self.liczba_operacji[indeks]

        self.index -= len(indeksy_do_usuniecia)

        # Tworzymy listę indeksów posortowanych według wartości w self.liczba
        posortowane_indeksy = sorted(range(len(self.liczba)), key=lambda i: self.liczba[i])

        # Tworzymy nowe listy z uporządkowanymi elementami
        self.liczba = [self.liczba[i] for i in posortowane_indeksy]
        self.sumy = [self.sumy[i] for i in posortowane_indeksy]
        self.liczba_operacji = [self.liczba_operacji[i] for i in posortowane_indeksy]




def main():
    l = Liczba()
    with open("wynik.txt") as f:
        for i, line in enumerate(f):
            parts = line.strip().split(";")  # Usuwa białe znaki i dzieli po ";"
            if len(parts) >= 3:  # Sprawdzamy, czy są wszystkie trzy wartości
                l.liczba.append(parts[0])
                l.sumy.append(parts[1])
                l.liczba_operacji.append(parts[2])
                l.index += 1  # Zwiększamy licznik wierszy
            else:
                pass

            if i >= 100:  # Ograniczenie dla testów
                break
    l.convert_to_int()
    l.filtr_list()

    
    l.print_f()  # Wywołujemy funkcję do wyświetlenia wyników

main()
