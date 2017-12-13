from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "Demo",
    ext_modules = cythonize('demo.pyx'),  # accepts a glob pattern
)