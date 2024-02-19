from enum import Enum
from typing import List

from translator import Arg


class Label:

    def __init__(self, name: str) -> None:
        self.name = name
        self.value: None | str | int = None

    def setValue(self, val: str | int) -> None:
        self.value = val

    def toJSON(self) -> dict:
        return {
            'name': self.name,
            'literal': self.value is not None,
            'value': self.value
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


class LLI(Enum):
    ALU1 = 'alu1'
    ALU2 = 'alu2'
    SUM = 'sum'
    WRITE_REG = 'write_reg'
    LABEL = 'label'


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
    arg: int | str | None = None
    if args is not None:
        assert args[0].name == 'word'
        assert len(args) > 1
        try:
            arg = int(args[1].name)
        except ValueError:
            arg = ' '.join([x.name for x in args[1::]])
        label.setValue(arg)
    return [
        Command(line_number, LLI.LABEL.value, label)
    ]
