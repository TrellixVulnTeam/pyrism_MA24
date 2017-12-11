#version 430

in vec2 texCoord0;
varying out vec3 color;

uniform sampler2D ColorTexture;
uniform sampler2D DepthTexture;

uniform vec2 texelSize;

float luminosity(in vec4 col) {
    return sqrt((0.299*pow(col.x, 2)) + (0.587*pow(col.y, 2)) + (0.114*pow(col.z, 2)));
}

float pixelLuminosity(in vec2 offset) {
    return luminosity(texture(ColorTexture, (texCoord0 + offset)*vec2(1.0,-1.0)));
}

float getSum(mat4 mat)
{
    vec4 vec = mat[0] + mat[1] + mat[2] + mat[3];
    return vec.x + vec.y + vec.z + vec.w;
}

float getSum(mat3 mat)
{
    vec3 vec = mat[0] + mat[1] + mat[2];
    return vec.x + vec.y + vec.z;

}

void main() {
    float middle = pixelLuminosity(vec2(0.0,0.0)*texelSize);

    float bottom = pixelLuminosity(vec2(0.0,1.0)*texelSize);
    float top = pixelLuminosity(vec2(0.0,-1.0)*texelSize);
    float left = pixelLuminosity(vec2(-1.0,0.0)*texelSize);
    float right = pixelLuminosity(vec2(1.0,0.0)*texelSize);

    float bottomleft = pixelLuminosity(vec2(-1.0, 1.0)*texelSize);
    float topright = pixelLuminosity(vec2(1.0,-1.0)*texelSize);
    float topleft = pixelLuminosity(vec2(-1.0,-1.0)*texelSize);
    float bottomright = pixelLuminosity(vec2(1.0,1.0)*texelSize);

    mat3 lums = mat3( topleft, top, topright,
                    left, middle, right,
                    bottomleft, bottom, bottomright );

    mat3 gx = mat3( -1.0, 0.0, 1.0,
                  -2.0, 0.0, 2.0,
                  -1.0, 0.0, 1.0 );

    mat3 gy = mat3( 1.0, 2.0, 1.0,
                  0.0, 0.0, 0.0,
                  -1.0, -2.0, -1.0 );

    gx *= lums;
    gy *= lums;

    float g = abs(getSum(gx))+ abs(getSum(gy));

    color = vec3(g,g,g);
}