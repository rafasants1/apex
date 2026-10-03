#include <math.h>
#include "estatistica.h"

double cauchy(double x) {
    return 1.0 / (M_PI * (1.0 + x * x));
}

double gumbel(double x, double mu, double beta) {
    double z = (x - mu) / beta;
    return (1.0 / beta) * exp(-(z + exp(-z)));
}

double laplace(double x, double mu, double b) {
    return (1.0 / (2.0 * b)) * exp(-fabs(x - mu) / b);
}
