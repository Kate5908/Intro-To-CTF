///R.O.P == Really Oawesome Program

#include <stdio.h>
#include <stdlib.h>

void init() {
	setvbuf(stdout, 0, _IONBF, 0);
	setvbuf(stderr, 0, _IONBF, 0);
}

int main() {
	init();

	char buf[0x100];

	puts("After beating the british oil execs, you've arrived here. Good luck!");
	gets(buf);
}
