import calcular_pi
import time

n = 10_000_000
print('===== PYTHON =====')
print(f'Calculando pi con n = {n:,}')
inicio = time.time()
resultado = calcular_pi.calcular_pi(n)
total = time.time() - inicio
print(f't = {total:.4f}s, pi = {resultado}')
