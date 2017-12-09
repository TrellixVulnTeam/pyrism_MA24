#version 430

in vec2 texCoord0;
layout(location = 0) out vec4 color;

layout(location = 1) uniform sampler2D ColorTexture;
layout(location = 2) uniform sampler2D DepthTexture;

layout(location = 3) uniform vec2 texelSize;

float luminosity(in vec4 col) {
    return sqrt((0.299*pow(col.x, 2)) + (0.587*pow(col.y, 2)) + (0.114*pow(col.z, 2)));
}

float colorLuminosity(in vec2 texCoordOffset) {
    float rv = luminosity(texture(ColorTexture, texCoord0 + texCoordOffset));
    return rv;
}

void main() {
    vec2 ts = vec2(1.0/800, 1.0/600);
    float lum = colorLuminosity(vec2(0,0));
   /*
    mat3x3 gx = lums*(-1, 0, 1,
                 -2, 0, 2,
                 -1, 0, 1);

    mat3x3 gy = lums*(-1, -2, -1,
                 0, 0, 0,
                 1, 2, 1);

    float g = abs(float(gx))+ abs(float(gy));
*/
    color = vec4(lum,lum,lum,1.0);
}