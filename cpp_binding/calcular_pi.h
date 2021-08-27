#include <pybind11/pybind11.h>

double calcular_pi(long num_rects);

PYBIND11_MODULE(calcular_pi, mod) {
    mod.def("calcular_pi_cpp", &calcular_pi, "Calcular pi.");
}
