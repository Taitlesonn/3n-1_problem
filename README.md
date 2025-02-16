# 3n-1 Problem

Projekt badający hipotezę Collatza (3n+1). Składa się z programu w C generującego liczby do analizy oraz skryptu Python analizującego wyniki.

## Struktura projektu
- **`main.c`** – program generujący liczby do badania.
- **`main`** – skompilowana wersja programu w C.
- **`alaiz3n/analiza.py`** – skrypt Python analizujący wygenerowane dane.
- **`alaiz3n/wynik.txt`** – plik z wynikami wygenerowanymi przez `main`.

## Kompilacja i uruchomienie
Aby skompilować program, użyj komendy:
```bash
gcc main.c -o main -lgmp -fopenmp
```

Następnie uruchom program:
```bash
./main
```

Po wygenerowaniu danych możesz uruchomić analizę w Pythonie:
```bash
#dla linuxa/macos
source alaiz3n/3n_projekt/bin/activate
#dla windows
.\nalaiz3n\3n_projekt\Scripts\activate


python3 alaiz3n/analiza.py

#żby wyjść:
deactivate
```

## Wymagania
- Kompilator `gcc` z obsługą `gmp` i `openmp`
- Python 3

## Autor
[Taitlesonn](https://github.com/Taitlesonn)

