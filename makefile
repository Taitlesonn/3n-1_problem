FLAGS = -O3 -lgmp -fopenmp

main.out: main.c
	gcc main.c -o out/main ${FLAGS}