start:

loop:
    in
    mov ebx eax
    cmp eax 1000
    jz end
    mov eax ebx
    out
    jnz loop

end: