import calcular_pi
import time

n = 10_000_000
print('===== C++ =====')
print(f'Calculando pi con n = {n:,}')
inicio = time.time()
resultado = calcular_pi.calcular_pi_cpp(n)
total = time.time() - inicio
print(f't = {total:.4f}s, pi = {resultado}')
