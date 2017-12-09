#version 430

in vec2 texCoord0;
out vec4 color;

uniform sampler2D sampler;

void main() {
	gl_FragColor = texture(sampler, texCoord0);
}
