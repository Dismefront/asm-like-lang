first_entry = 0
second_entry = 0


def put_first_entry(a: str) -> None:
    global first_entry
    try:
        first_entry = int(a)
    except ValueError:
        first_entry = ord(a)


def put_second_entry(a: str) -> None:
    global second_entry
    try:
        second_entry = int(a)
    except ValueError:
        second_entry = ord(a)


def sub_signal() -> int:
    global first_entry, second_entry
    return first_entry - second_entry


def add_signal() -> int:
    global first_entry, second_entry
    return first_entry + second_entry
