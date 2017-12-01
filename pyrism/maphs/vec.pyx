ctypedef struct vec2i:
    int x, y

ctypedef struct vec3i:
    int x, y, z

ctypedef struct vec2f:
    float x, y

ctypedef struct vec3f:
    float x, y, z

# for testing purposes only
cdef vec3f v1
v1.x = 20.0
v1.y = 12.5
v1.z = 2.87

cdef vec3f v2
v2.x = 12.8
v2.y = 86.6
v2.z = 67.2

def add_vec3f():
    cdef vec3f v
    v.x = v1.x + v2.x
    v.y = v1.y + v2.y
    v.z = v1.z + v2.z
    return v