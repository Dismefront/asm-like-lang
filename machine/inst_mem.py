from typing import Dict, List

from machine.commands import Command, LLI


instructions: List[Command] = []
label_mapper: Dict[str, int] = dict()


def save_instructions(data: List[Command]) -> None:
    global instructions
    instructions = data
    for inst in instructions:
        if inst.optype == LLI.LABEL.value:
            assert inst.arg is not None
            label_mapper[inst.arg.name] = inst.op


def get_instruction(instruction_num: int) -> Command:
    global instructions
    return instructions[instruction_num]
