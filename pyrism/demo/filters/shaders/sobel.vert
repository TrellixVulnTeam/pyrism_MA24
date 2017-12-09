#version 430

in vec4 position;
in vec2 texCoord;

out vec2 texCoord0;

void main() {
	gl_Position = position;
    texCoord0 = texCoord;
}
