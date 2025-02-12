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
    l.print_f()  # Wywołujemy funkcję do wyświetlenia wyników

main()
