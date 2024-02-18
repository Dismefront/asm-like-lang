from enum import Enum
import json
from typing import List
from translator import CiscCommand, Arg


class Label:

    def __init__(self, name: str) -> None:
        self.name = name

    def setOpCode(self, no: int) -> None:
        self.opCode = no

    def toJSON(self) -> dict:
        return {
            'name': self.name,
            'opCode': self.opCode
        }


class Command:
    op_no = 1

    def __init__(self,
                 line_number: int,
                 optype: str,
                 arg: Arg | Label | None) -> None:
        self.line_number = line_number
        self.optype = optype
        self.arg = arg
        self.op = Command.op_no
        Command.op_no += 1
        if isinstance(self.arg, Label):
            self.arg.setOpCode(self.op_no)

    def toJSON(self) -> dict:
        arg = None
        if self.arg is not None:
            arg = self.arg.toJSON()
        return {
            'line_number': self.line_number,
            'optype': self.optype,
            'operation_number': self.op,
            'arg': arg
        }


def add(line_number: int, args: List[Arg] | None) -> List[Command]:
    assert args is not None
    return [
        Command(line_number, LLI.ALU1.value, args[0]),
        Command(line_number, LLI.ALU2.value, args[1]),
        Command(line_number, LLI.SUM.value, None),
        Command(line_number, LLI.WRITE_REG.value, args[0])
    ]


def label(name: str,
          line_number: int,
          args: List[Arg] | None) -> List[Command]:
    label = Label(name)
    return [
        Command(line_number, LLI.LABEL.value, label)
    ]


class LLI(Enum):
    ALU1 = 'alu1'
    ALU2 = 'alu2'
    SUM = 'sum'
    WRITE_REG = 'write_reg'
    PC_INC = 'pc_inc'
    LABEL = 'label'
    WORD = 'word'


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
    'out': add
}


def generate_mc(commands: List[CiscCommand]) -> None:
    mc: List[Command] = []
    for command in commands:
        if command.instruction[-1] == ":":
            if command.args is None:
                mc += label(command.instruction[:-1],
                            command.line_number,
                            command.args)
            else:
                pass
        else:
            decoded = INSTRUCTIONS[command.instruction]
            mc += decoded(command.line_number, command.args)

    print(json.dumps([x.toJSON() for x in mc], indent=2))
