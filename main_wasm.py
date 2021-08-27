from wasmer import engine, wat2wasm, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler
import time

with open('calcular_pi.wat') as archivo:
    wasm_text = archivo.read()
wasm_bytes = wat2wasm(wasm_text)
store = Store(engine.JIT(Compiler))
module = Module(store, wasm_bytes)
instance = Instance(module)
calcular_pi = instance.exports.calcular_pi

n = 10_000_000
print('===== WASM =====')
print(f'Calculando pi con n = {n:,}')
inicio = time.time()
resultado = calcular_pi(n)
total = time.time() - inicio
print(f't = {total:.4f}s, pi = {resultado}')
