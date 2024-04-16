# Writeup
- Meant to be follow-up to british-oil-company
- Stack is no longer leaked for us, and the stack itself is no longer executable
- However, we disabled PIE on this one.
- gets still gives trivial buffer-overflow
- Where do we redirect execution to?
- Use `ropr` or similar tool to find ROP gadgets in the binary
- Load `rdi` to the addr of a GOT entry (thus, a lib address), then call `puts` (which we convenientry give), before returning to main
- If done correctly, we are at the start of main, with a libc leak
- Calculate the libc base address. Then, use `ropr` again, but on the libc this time
- Create a ropchain to get shell, and feed it to the program.

