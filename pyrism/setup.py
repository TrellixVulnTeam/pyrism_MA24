from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext


ext_modules=[
    Extension("shapes",    # location of the resulting .so
             ["shapes.pyx", "shapes.pxd"],) ]

setup(name='pyrism',
      packages=find_packages(),
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules,
     )