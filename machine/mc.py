from typing import List
from machine.commands import \
    add, label, mov, sub, cmp
from translator.tokenizer import CiscCommand


INSTRUCTIONS = {
    'add': add,
    'mov': mov,
    'sub': sub,
    'cmp': cmp,
    'inc': add,
    'dec': add,
    'jmp': add,
    'jnz': add,
    'jz': add,
    'in': add,
    'out': add,
    'call': add,
    'ret': add
}


def generate_mc(commands: List[CiscCommand]) -> List:
    mc = []
    for command in commands:
        if command.instruction[-1] == ":":
            if command.args is None:
                mc += label(command.instruction[:-1],
                            command.line_number,
                            command.args)
            else:
                mc += label(command.instruction[:-1],
                            command.line_number,
                            command.args)
        else:
            decoded = INSTRUCTIONS[command.instruction]
            mc += decoded(command.line_number, command.args)

    return mc
