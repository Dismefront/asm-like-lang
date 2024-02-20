from enum import Enum
from typing import List
from machine.data_mem import put_int, put_str, alloc_buffer

from translator.tokenizer import Arg


class Label:

    def __init__(self, name: str) -> None:
        self.name = name
        self.value: None | str | int = None
        self.immed = True

    def setValue(self, val: str | int) -> None:
        self.value = val
        if isinstance(self.value, str):
            self.immed = False

    def toJSON(self) -> dict:
        return {
            'name': self.name,
            'immed': self.immed,
            'value': self.value
        }


class Command:
    op_no = 0

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
    ALU_SIG_SUM = 'sum'
    ALU_SIG_SUB = 'sub'
    INC = 'inc'
    DEC = 'dec'
    WRITE_FROM_ALU = 'write_from_alu'
    WRITE_TO_BUF_REG = 'write_to_bufreg'
    WRITE_BUF_TO_REG = 'write_buf_to_reg'
    LABEL = 'label'


def dec(line_number: int, args: List[Arg] | None) -> List[Command]:
    assert args is not None and len(args) == 1
    return [
        Command(line_number, LLI.DEC.value, args[0])
    ]


def inc(line_number: int, args: List[Arg] | None) -> List[Command]:
    assert args is not None and len(args) == 1
    return [
        Command(line_number, LLI.INC.value, args[0])
    ]


def cmp(line_number: int, args: List[Arg] | None) -> List[Command]:
    assert args is not None and len(args) == 2
    eax = Arg('eax')
    return [
        Command(line_number, LLI.ALU1.value, args[0]),
        Command(line_number, LLI.ALU2.value, args[1]),
        Command(line_number, LLI.ALU_SIG_SUB.value, None),
        Command(line_number, LLI.WRITE_FROM_ALU.value, eax)
    ]


def mov(line_number: int, args: List[Arg] | None) -> List[Command]:
    assert args is not None and len(args) == 2
    return [
        Command(line_number, LLI.WRITE_TO_BUF_REG.value, args[1]),
        Command(line_number, LLI.WRITE_BUF_TO_REG.value, args[0])
    ]


def sub(line_number: int, args: List[Arg] | None) -> List[Command]:
    assert args is not None and len(args) == 2
    return [
        Command(line_number, LLI.ALU1.value, args[0]),
        Command(line_number, LLI.ALU2.value, args[1]),
        Command(line_number, LLI.ALU_SIG_SUB.value, None),
        Command(line_number, LLI.WRITE_FROM_ALU.value, args[0])
    ]


def add(line_number: int, args: List[Arg] | None) -> List[Command]:
    assert args is not None and len(args) == 2
    return [
        Command(line_number, LLI.ALU1.value, args[0]),
        Command(line_number, LLI.ALU2.value, args[1]),
        Command(line_number, LLI.ALU_SIG_SUM.value, None),
        Command(line_number, LLI.WRITE_FROM_ALU.value, args[0])
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
            if arg <= 20:
                alloc_buffer(name, arg)
            else:
                put_int(name, arg)
        except ValueError:
            arg = ' '.join([x.name for x in args[1::]]).strip('\"')
            put_str(name, arg)
        return []
    return [
        Command(line_number, LLI.LABEL.value, label)
    ]
