import json
from typing import List


class CiscCommand:

    def __init__(self, ln_no: int, line: str) -> None:
        self.line_number = ln_no
        tokens = line.split(" ")
        self.instruction = tokens[0]
        self.args: None | List[Arg] = None
        if len(tokens) <= 1:
            return
        self.args = [Arg(token) for token in tokens[1:]]

    def __str__(self) -> str:
        args = None
        if self.args is not None:
            args = [x.toJSON() for x in self.args]
        return json.dumps({
            "line": self.line_number,
            "instruction": self.instruction,
            "args": args
        }, indent=2)


class Arg:

    def __init__(self, token: str) -> None:
        self.name = token

    def __str__(self) -> str:
        return json.dumps({
            "name": self.name
        }, indent=2)

    def toJSON(self) -> dict:
        return {
            "name": self.name
        }


def tokenize(source: str) -> List[CiscCommand]:
    src_file = open(source, "r")
    parsed_list: List[CiscCommand] = []
    for idx, line in enumerate(src_file):
        line = line.strip()
        if line == "":
            continue
        command = CiscCommand(idx + 1, line)
        parsed_list.append(command)
    return parsed_list
