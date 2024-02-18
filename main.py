import sys
from translator.tokenizer import tokenize

if __name__ == "__main__":
    assert len(sys.argv) == 4, \
        "Wrong arguments: main.py <program> <input_device> <output_device>"
    program_url = sys.argv[1]
    inp_device_url = sys.argv[2]
    out_device_url = sys.argv[3]

    parsed_commands = tokenize(program_url)  # Первый этап обработки кода
