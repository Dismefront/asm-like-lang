import json
import sys
from typing import List
from machine.commands import Command
from translator.tokenizer import tokenize
from machine.mc import generate_mc
from machine.inst_mem import save_instructions
from machine.control import start, set_devices, set_debug_output
from machine.data_mem import data_memory

debug = open('./devices/debug', 'w')

if __name__ == "__main__":
    assert len(sys.argv) == 4, \
        "Wrong arguments: main.py <program> <input_device> <output_device>"
    program_url = sys.argv[1]
    inp_device_url = sys.argv[2]
    out_device_url = sys.argv[3]
    set_devices(inp_device_url, out_device_url)
    set_debug_output(debug)

    ast = tokenize(program_url)
    mc: List[Command] = generate_mc(ast)
    save_instructions(mc)
    start()

    # debug
    # import json
    debug.write(json.dumps([x.toJSON() for x in mc], indent=2))
    # print([(x, data_memory_mapper[x]) for x in list(data_memory_mapper)])
    print(data_memory[:50])
