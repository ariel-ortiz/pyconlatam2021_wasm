#
# Para compilar e instalar:
#
#   pip install -e .
#

from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

example_module = Pybind11Extension(
    'calcular_pi',
    [str(fname) for fname in Path('.').glob('*.cpp')],
    extra_compile_args=['-O3']
)

setup(
    name='calcular_pi',
    version=0.1,
    author='Sin Nombre',
    author_email='sin_nombre@example.com',
    description='Ejemplo para calcular el valor de pi',
    ext_modules=[example_module],
    cmdclass={"build_ext": build_ext},
)
