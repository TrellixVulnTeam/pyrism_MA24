#version 430

in vec2 texCoord0;
layout(location = 0) out vec4 color;

uniform sampler2D ColorTexture;
uniform sampler2D DepthTexture;

void main() {
    color = texCoord0.x-texture(ColorTexture, texCoord0+vec2(0, sin(texCoord0.x*10)*0.1));
}