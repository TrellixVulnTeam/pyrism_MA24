#!/usr/bin/env python

import numpy as np

import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule

mod = SourceModule("""
__global__ void cuda_dbl(float *dest, float *a)
{
    const int i = threadIdx.x;
    dest[i] = 2.*a[i];
}
""")

cuda_dbl = mod.get_function("cuda_dbl")

n = 10
a = np.full(n, 10, dtype=np.float32)
ans = np.zeros_like(a)

cuda_dbl(drv.Out(ans), drv.In(a), block=(n, 1, 1), grid=(1, 1))

print(ans)