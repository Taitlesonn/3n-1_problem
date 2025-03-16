# imports
import matplotlib.pyplot as plt

class Liczba:
    def __init__(self):
        self.liczba = []
        self.sumy = []
        self.liczba_operacji = []
        self.index = 0

    def print_f(self):
        for i in range(len(self.liczba)):
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
        Przez to że w naszym programie stawiamy na wydajność, nie dokładność,
        część liczb może być obliczana wielokrotnie.
        Ta funkcja zajmie się odfiltrowaniem powtarzających się elementów,
        a następnie posortuje listę.
        """
        seen = set()  # zbiór do śledzenia już widzianych liczb
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

        # Sortowanie według wartości w self.liczba
        posortowane_indeksy = sorted(range(len(self.liczba)), key=lambda i: self.liczba[i])
        self.liczba = [self.liczba[i] for i in posortowane_indeksy]
        self.sumy = [self.sumy[i] for i in posortowane_indeksy]
        self.liczba_operacji = [self.liczba_operacji[i] for i in posortowane_indeksy]
    
    def call_rel(self, t: int):
        """
        Agreguje dane w grupach po 100 elementów.
        Jeśli t == 0, agreguje dane z self.sumy,
        jeśli t == 1, agreguje dane z self.liczba_operacji.
        """
        i = 0
        lista_r = []
        # Upewniamy się, że nie wychodzimy poza zakres danych
        n = len(self.liczba)
        while i < n:
            suma = 0
            # Jeśli mamy mniej niż 100 elementów na końcu, używamy ich wszystkich
            grupa = self.sumy[i:i+1000] if t == 0 else self.liczba_operacji[i:i+100]
            if not grupa:
                break
            for wartosc in grupa:
                suma += wartosc
            lista_r.append(suma / len(grupa))
            i += 1000
        return lista_r

    def get_x_aggregated(self):
        """
        Oblicza zagregowane wartości dla osi X, np. średnią z 100-elementowych grup z self.liczba.
        """
        x_agg = []
        i = 0
        n = len(self.liczba)
        while i < n:
            grupa = self.liczba[i:i+1000]
            if grupa:
                x_agg.append(sum(grupa) / len(grupa))
            i += 1000
        return x_agg

    def draw_graf_liczba_do_sumy(self):
        # Wykres oryginalnych danych
        plt.plot(self.liczba, self.sumy, label="Dane oryginalne")
        # Wykres zagregowanych danych (średnia co 100 elementów)
        x_agg = self.get_x_aggregated()
        y_agg = self.call_rel(0)
        plt.plot(x_agg, y_agg, color="red", label="Średnia co 1000 elementów")
        plt.xlabel("Liczba")
        plt.ylabel("Suma")
        plt.title("Liczba do sumy")
        plt.legend()
        plt.show()

    def draw_graf_il_operacji_do_liczby(self):
        plt.plot(self.liczba, self.liczba_operacji, label="Dane oryginalne")
        x_agg = self.get_x_aggregated()
        y_agg = self.call_rel(1)
        plt.plot(x_agg, y_agg, color="red", label="Średnia co 1000 elementów")
        plt.xlabel("Liczba")
        plt.ylabel("Liczba operacji")
        plt.title("Ilość operacji do liczby")
        plt.legend()
        plt.show()

    

def main():
    l = Liczba()
    try:
        with open("wynik.txt", encoding="utf-8") as f:
            for i, line in enumerate(f):
                parts = line.strip().split(";")  # Usuwamy białe znaki i dzielimy po ";"
                if len(parts) >= 3:  # Sprawdzamy, czy mamy wszystkie trzy wartości
                    l.liczba.append(parts[0])
                    l.sumy.append(parts[1])
                    l.liczba_operacji.append(parts[2])
                    l.index += 1  # Zwiększamy licznik wierszy
                else:
                    pass

                # Ograniczenie dla testów
                if i >= 10000000:
                    break
    except FileNotFoundError as e:
        print(f"Nie znaleziono pliku: {e}")
        return

    l.convert_to_int()
    l.filtr_list()

    # Rysujemy wykresy
    l.draw_graf_liczba_do_sumy()
    l.draw_graf_il_operacji_do_liczby()
    # l.print_f()  # Opcjonalnie, do wyświetlenia przetworzonych danych

if __name__ == "__main__":
    main()
