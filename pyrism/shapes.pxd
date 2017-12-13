cdef struct vec3:
    float x, y, z
ctypedef vec3 Vector
ctypedef vec3 Point
ctypedef packed struct Sphere:
    Point center
    float radius
ctypedef packed struct Ellipse:
    Point center
    float radius
    Vector size # a*x^2 + b*y^2 + c*z^2 + r^2 = 0 is the function for
#  modeling a 3-Dimensional ellipse where a, b and c are size.x, size.y and size.z respectively.
ctypedef packed struct Box:
    Point center
    Vector size
ctypedef struct RoundedBox:
    Point center
    Vector size
    float radius # this is to define the radius distance of the
#  sphere being averaged with the box distance.

cdef Vector add(const Vector*, const Vector*)

cdef inline void test():
    print("testing")