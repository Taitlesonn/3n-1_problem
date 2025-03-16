FLAGS = -O3 -lgmp -fopenmp -Werror

main.out: main.c
	gcc main.c -o out/$@ ${FLAGS}
	./out/$@
