question: word "What is your name?"
greet: word " Hello, "
username: word 12

start:
    mov ebx question
    mov ecx 1

print_question:
    inc ebx
    mov eax [ebx]
    jz get_username
    out
    jnz print_question
    

get_username:
    in
    mov ebx eax
    cmp eax 1000
    jz end_get_username
    mov [username+ecx] ebx
    inc ecx
    jnz get_username

end_get_username:
    mov ecx 1
    mov ebx greet

print_greeting:
    inc ebx
    mov eax [ebx]
    jz end_print_greeting
    out
    jnz print_greeting

end_print_greeting:
    mov ecx 1

print_username:
    mov eax [username+ecx]
    mov ebx eax
    cmp 0 [username+ecx]
    jz end
    mov eax ebx
    out
    inc ecx
    jnz print_username

end: