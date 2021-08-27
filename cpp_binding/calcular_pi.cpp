#include "calcular_pi.h"

double calcular_pi(long num_rects) {
    double suma = 0.0;
    double ancho = 1.0 / num_rects;
    for (long i = 0; i < num_rects; i++) {
        double medio = (i + 0.5) * ancho;
        double alto = 4.0 / (1.0 + medio * medio);
        suma += alto;
    }
    return ancho * suma;
}
