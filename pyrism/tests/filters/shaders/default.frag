#version 430

in vec2 texCoord0;
layout(location = 0) out vec4 color;

uniform sampler2D sampler;

void main() {
    color = texture(sampler, texCoord0);
}