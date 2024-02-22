from main import prog


def prob2_test() -> None:
    log_path = './devices/debug'
    out_path = './devices/output.out'

    prog('./devices/prob2.asm',
         './devices/input.in',
         './devices/output.out')

    log_content = read_file(log_path)
    out_content = read_file(out_path)
    compared_content_log = read_file('./snapshots/prob2.log')
    compared_content_out = read_file('./snapshots/prob2.out')

    assert log_content == compared_content_log
    assert out_content == compared_content_out
    print("----------------prob2 test success----------------")


def read_file(src: str) -> str:
    with open(src, 'r') as file:
        s = ''.join(file.readlines())
    return s


if __name__ == '__main__':
    prob2_test()
