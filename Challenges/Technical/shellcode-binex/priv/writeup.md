# Writeup
- Stack address is leaked to us, defeating ASLR for the stack
- gets gives us a trivial buffer overflow
- Check the protections for the binary - stack is executable (odd), and not stack canary
- Executable stack probably means shellcode. 
- Pull a standard payload from somewhere "execve shellcode". Prepend it with NOP bytes for extra stability, so that if we redirect execution to somewhere early in the buffer it just slides down to the actual code
- Send payload (NOPS + execve shellcode), then overwrite saved RIP to the stack address we give (that of the buffer)
