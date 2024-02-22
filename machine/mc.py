from typing import List
from machine.commands import \
    add, label, mov, sub, compare, \
    inc, dec, jz, jnz, io_in, io_out, \
    cmd_exit, cmd_mod, jn, jmp
from translator.tokenizer import CiscCommand


INSTRUCTIONS = {
    'add': add,
    'mov': mov,
    'sub': sub,
    'cmp': compare,
    'inc': inc,
    'dec': dec,
    'jnz': jnz,
    'jz': jz,
    'in': io_in,
    'out': io_out,
    'call': add,
    'ret': add,
    'exit': cmd_exit,
    'mod': cmd_mod,
    'jn': jn,
    'jmp': jmp
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
