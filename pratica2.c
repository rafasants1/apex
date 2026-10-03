#include <stdio.h>
#include "estatistica.h"

int main() {
    printf("cauchy(x=-2): %f\n", cauchy(-2));
    printf("gumbel(x=0, mu=0.5, beta=2): %f\n", gumbel(0, 0.5, 2));
    printf("laplace(x=-6, mu=-5, b=4): %f\n", laplace(-6, -5, 4));
    return 0;
}
