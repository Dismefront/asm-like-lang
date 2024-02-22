import re
from machine.alu import put_first_entry, put_second_entry, sub_signal
from machine.commands import Command, LLI
from machine.inst_mem import get_instruction
from machine.data_mem import data_memory, data_memory_mapper as dmm
from machine.inst_mem import label_mapper

dmm, data_memory

eax = 0
ebx = 0
ecx = 0
edx = 0
esp = 100000
eip = 0
tick = 0
tmp: int | str = 0
alu_res = 0


def parse_lang(exp: str) -> str:
    pattern = r'\b(?!eax|ebx|ecx|edx|esp|eip)[a-zA-Z0-9]+'
    matches = re.findall(pattern, exp)
    for match in matches:
        try:
            int(match)
        except ValueError:
            exp = exp.replace(match, f'dmm["{match}"][0]', 1)
    if exp[-1] == ']' and exp[0] == '[':
        exp = 'data_memory' + exp
    return exp


def handle_next() -> None:
    global eip, eax, ebx, ecx, edx, eip, tmp
    global alu_res
    command: Command = get_instruction(eip)
    eip += 1
    match command.optype:
        case LLI.WRITE_TO_BUF_REG.value:
            assert command.arg is not None
            var = 'edx=' + parse_lang(command.arg.name)
            exec(var, globals())
        case LLI.WRITE_BUF_TO_REG.value:
            assert command.arg is not None
            var = parse_lang(command.arg.name) + '=' + 'edx'
            exec(var, globals())
        case LLI.OUT.value:
            print("out: ", eax)
        case LLI.ALU1.value:
            assert command.arg is not None
            var = parse_lang(command.arg.name)
            exec('tmp=' + var, globals())
            put_first_entry(str(tmp))
        case LLI.ALU2.value:
            assert command.arg is not None
            var = parse_lang(command.arg.name)
            exec('tmp=' + var, globals())
            put_second_entry(str(tmp))
        case LLI.ALU_SIG_SUB.value:
            alu_res = sub_signal()
        case LLI.WRITE_FROM_ALU.value:
            assert command.arg is not None
            var = parse_lang(command.arg.name) + '=' + str(alu_res)
            exec(var, globals())
        case LLI.JNZ.value:
            assert command.arg is not None
            if eax != 0:
                eip = label_mapper[command.arg.name]
        case LLI.JZ.value:
            assert command.arg is not None
            if eax == 0:
                eip = label_mapper[command.arg.name]
        case LLI.INC.value:
            assert command.arg is not None
            var = parse_lang(command.arg.name)
            var = var + '=' + var + '+1'
            exec(var, globals())
    print(eax, ebx, ecx, edx, eip, label_mapper)


def start() -> None:
    while True:
        try:
            handle_next()
        except IndexError:
            break
    print('program finished')
