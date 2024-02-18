import sys
from translator import tokenize
from machine import generate_mc

if __name__ == "__main__":
    assert len(sys.argv) == 4, \
        "Wrong arguments: main.py <program> <input_device> <output_device>"
    program_url = sys.argv[1]
    inp_device_url = sys.argv[2]
    out_device_url = sys.argv[3]

    ast = tokenize(program_url)
    generate_mc(ast)
