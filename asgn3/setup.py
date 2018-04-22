from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

extensions = [
  Extension('im2col_cython', ['im2col_cython.pyx'],
            include_dirs = ["/home/fubao/.local/share/jupyter/kernels/python2"]
  ),
]

setup(
    ext_modules = cythonize(extensions),
)
