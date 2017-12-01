ctypedef struct vec2i:
    int x, y

ctypedef struct vec3i:
    int x, y, z

ctypedef struct vec2f:
    float x, y

ctypedef struct vec3f:
    float x, y, z

class Vec3f(object):
    cpdef void test(self):
        print('testing')

def add_vec3f(vec3f a, vec3f b):
    cdef vec3f v
    v.x = a.x + b.x
    v.y = a.y + b.y
    v.z = a.z + b.z
    return v