from libc.math cimport sqrt
from shapes cimport *

cdef float magnitude(const Vector *v):
        return sqrt(v.x**2 + v.y**2 + v.z**2)
cdef Vector add(const Vector *a, const Vector *b):
    cdef Vector rv
    rv.x = a.x + b.x
    rv.y = a.y + b.y
    rv.z = a.z + b.z
    return rv
cdef Vector sub(const Vector *a, const Vector *b):
    cdef Vector rv
    rv.x = a.x - b.x
    rv.y = a.y - b.y
    rv.z = a.z - b.z
    return rv
cdef Vector mul(const Vector *v, float x):
    cdef Vector rv
    rv.x = v.x*x
    rv.y = v.y*x
    rv.z = v.z*x
    return rv
cdef Vector div(const Vector *v, float x):
    cdef Vector rv
    rv.x = v.x/x
    rv.y = v.y/x
    rv.z = v.z/x
    return rv