# WebAssembly + Python

**NOTA:** Las siguientes instrucciones suponen que se tiene un ambiente tipo Unix, por ejemplo macOS, Linux o WSL (subsistema de Windows para Linux) con Python versión 3.6 o superior.

## Pyodide

Correr un servidor HTTP desde la terminal:

    python -m http.server

En el navegador (versión reciente de Chrome, Firefox, Safari o Edge) solicitar el siguiente URL:

    localhost:8000

El código de Python a ejecutar en el navegador está contenido en el archivo `calcular_pi.py`. El archivo `index.html` contiene el código de JavaScript necesario para interactuar con [Pyodide](https://pyodide.org/).

## Python puro

Correr desde la terminal:

    python main_python.py

El código de Python a ejecutar está en el módulo correspondiente al archivo `calcular_pi.py`.

## WebAssembly usando Wasmer

Se debe instalar primero [Wasmer](https://github.com/wasmerio/wasmer-python). Desde la terminal, teclear:

    pip install wasmer==1.0.0

    pip install wasmer_compiler_cranelift==1.0.0

Posteriormente, teclear en la terminal:

    python main_wasm.py

El código de WebAssembly a ejecutar está en formato de Wasm textual en el archivo `calcular_pi.wat`. El código original se escribió en C++ (corresponde al contenido del archivo `cpp_binding/calcular_pi.cpp`) y para producir el código Wat se utilizó el compilador _Emscripten_ disponible en línea desde [WebAssembly Studio](https://webassembly.studio/).

## Enlace con código en C++

Primero se debe instalar el módulo `pybind11`. Teclear desde la terminal:

    pip install pybind11

Luego se debe generar el enlace propiamente dicho del código de C++. Teclear:

    cd cpp_binding

    make

Finalmente, correr un programa de Python que utilice el enlace con C++:

    python main_cpp.py

El código de C++ a ejecutar está contenido en el archivo `cpp_binding/calcular_pi.cpp`.
