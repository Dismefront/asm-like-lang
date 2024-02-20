from typing import Dict, List, Tuple


data_memory_mapper: Dict[str, Tuple[int, int, int | str]] = dict()
mem_addr = 0

data_memory: List[int | str] = [0] * 200000


def put_int(name: str, value: int) -> None:
    global mem_addr
    varsize = 1
    data_memory[mem_addr] = value
    data_memory_mapper[name] = (
        mem_addr,
        varsize,
        value
    )
    mem_addr += varsize + 1


def alloc_buffer(name: str, value: int) -> None:
    global mem_addr
    varsize = 1
    data_memory[mem_addr] = value
    data_memory_mapper[name] = (
        mem_addr,
        varsize,
        value
    )
    mem_addr += varsize + value + 1


def put_str(name: str, value: str) -> None:
    global mem_addr
    varsize = len(value)
    data_memory[mem_addr] = varsize
    mem_addr += 1
    data_memory_mapper[name] = (
        mem_addr,
        varsize,
        value
    )
    j = 0
    for i in range(mem_addr, mem_addr + varsize):
        data_memory[i] = value[j]
        j += 1
    mem_addr += varsize + 1
