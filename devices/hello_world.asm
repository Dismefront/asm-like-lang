word: word "Hello world!"

start:
    mov ebx word

loop:
    inc ebx
    mov eax [ebx]
    jz end
    out
    jnz loop

end: