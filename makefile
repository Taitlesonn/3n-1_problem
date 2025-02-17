main.out: main.c
	gcc main.c -o out/main -lgmp -fopenmp