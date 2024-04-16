////british-oil-company == shell
////It's like, a reference. Please ignore that the actual British Petroleum company already exists.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void init() {
	setvbuf(stdout, 0, _IONBF, 0);
	setvbuf(stderr, 0, _IONBF, 0);
}

int main() {
	init();

	char buf[0x100];

	puts("Welcome to, like, the second 1511 program you'd ever write");

	////I love when challenges give us extra information. This surely has no role in exploiting the program.
	printf("What's your name? For peace of mind, I'll tell you that we're storing the data at %p.\n", buf);
	gets(buf);

	//Wonder if I mispelt her name, oh well
	if (strcmp(buf, "sasha") == 0)
		printf("My goodness, a celebrity!!!!");
}
