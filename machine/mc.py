from typing import List
from machine import add, label
from translator import CiscCommand


INSTRUCTIONS = {
    'add': add,
    'mov': add,
    'sub': add,
    'cmp': add,
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
