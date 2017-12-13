#include <stdio>

class Vector {
    public:
    Vector(float x = 0, float y = 1, float z = 0) : x(x), y(y), z(z){};
    virtual ~Vector();
    inline float length(){ return sqrt(x^2 + y^2 + z^2); };
    private:
    float x, y, z;
}