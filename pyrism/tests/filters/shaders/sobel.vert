#version 430

layout(location = 0) in vec4 position;
layout(location = 1) in vec2 texCoord;

out vec2 texCoord0;
void main() {
    gl_Position = position;
    texCoord0 = texCoord;
}
