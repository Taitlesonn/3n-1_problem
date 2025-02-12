#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <omp.h>

// Funkcja oblicza ciąg Collatza dla danej liczby początkowej 'start'
// i zwraca dynamicznie zaalokowany łańcuch znaków reprezentujący sumę kolejnych wartości ciągu (w systemie dziesiętnym).
// Liczba operacji (kroków) zostaje zwrócona przez parametr op_count.
char* collatz_sequence(int start, int *op_count) {
    mpz_t current, sum;
    mpz_init_set_ui(current, start);
    mpz_init(sum);
    mpz_set_ui(sum, 0);
    
    int count = 0;
    while (mpz_cmp_ui(current, 1) != 0) {
        // Jeśli liczba jest parzysta
        if (mpz_even_p(current)) {
            mpz_divexact_ui(current, current, 2);
        } else {
            // Jeśli liczba jest nieparzysta: current = 3 * current + 1
            mpz_mul_ui(current, current, 3);
            mpz_add_ui(current, current, 1);
        }
        mpz_add(sum, sum, current);
        count++;
    }
    
    // Zamieniamy wynik sumy na łańcuch znaków (system dziesiętny)
    char *sum_str = mpz_get_str(NULL, 10, sum);
    *op_count = count;
    
    mpz_clear(current);
    mpz_clear(sum);
    
    return sum_str;
}

int main(void) {
    int n;
    printf("Podaj liczbę (górna granica pętli, np. 1000): ");
    if (scanf("%d", &n) != 1) {
        fprintf(stderr, "Błąd odczytu liczby.\n");
        return 1;
    }
    
    FILE *fp = fopen("wynik.txt", "w");
    if (!fp) {
        perror("Nie można otworzyć pliku wynik.txt");
        return 1;
    }
    
    // Równoległe obliczanie dla kolejnych liczb od 5 do n-1
    #pragma omp parallel for schedule(dynamic)
    for (int i = 5; i < n; i++) {
        int op_count;
        char *sum_str = collatz_sequence(i, &op_count);
        
        // Krytyczna sekcja zabezpieczająca zapis do pliku
        #pragma omp critical
        {
            fprintf(fp, "%d;%s;%d\n", i, sum_str, op_count);
        }
        
        free(sum_str); // Zwalniamy pamięć zaalokowaną przez mpz_get_str
    }
    
    fclose(fp);
    return 0;
}
