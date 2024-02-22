import json
import sys
from typing import List
from machine.commands import Command
from translator.tokenizer import tokenize
from machine.mc import generate_mc
from machine.inst_mem import save_instructions
from machine.control import start, set_devices, set_debug_output
from machine.data_mem import data_memory
from machine.control import close_streams


def prog(program_url: str, inp_device_url: str, out_device_url: str) -> None:
    set_devices(inp_device_url, out_device_url)
    debug = open('./devices/debug', 'w')
    set_debug_output(debug)

    ast = tokenize(program_url)
    mc: List[Command] = generate_mc(ast)
    debug.write(json.dumps([x.toJSON() for x in mc], indent=2) + '\n')
    save_instructions(mc)
    start()

    # debug
    # import json
    # print([(x, data_memory_mapper[x]) for x in list(data_memory_mapper)])
    print(data_memory[:50])
    debug.close()
    close_streams()


if __name__ == "__main__":
    assert len(sys.argv) == 4, \
        "Wrong arguments: main.py <program> <input_device> <output_device>"
    program_url = sys.argv[1]
    inp_device_url = sys.argv[2]
    out_device_url = sys.argv[3]
    prog(program_url, inp_device_url, out_device_url)
