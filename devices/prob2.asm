limit: word 4000000
start:
    mov ebx 1
    mov ecx 2
    mov [esp] 2

loop:
    add ebx ecx
    mod ebx 2
    jz add_to_sum
    jnz swap
continue:
    cmp [limit] ebx
    jn end
    jz end
    jmp loop

add_to_sum:
    add [esp] ebx
    jmp swap

swap:
    mov eax ecx
    mov ecx ebx
    mov ebx eax
    jmp continue

end:
    mov eax [esp]
    out
