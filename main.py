import sys
from typing import List
from machine import Command
from translator import tokenize
from machine import generate_mc
from machine.data_mem import data_memory_mapper, data_memory

if __name__ == "__main__":
    assert len(sys.argv) == 4, \
        "Wrong arguments: main.py <program> <input_device> <output_device>"
    program_url = sys.argv[1]
    inp_device_url = sys.argv[2]
    out_device_url = sys.argv[3]

    ast = tokenize(program_url)
    mc: List[Command] = generate_mc(ast)
    import json
    print(json.dumps([x.toJSON() for x in mc], indent=2))
    print([(x, data_memory_mapper[x]) for x in list(data_memory_mapper)])
    print(data_memory[:20])
