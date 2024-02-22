from main import prog


def test_cat() -> None:
    log_path = './devices/debug'
    out_path = './devices/output.out'

    prog('./devices/cat.asm',
         './devices/input.in',
         './devices/output.out')

    log_content = read_file(log_path)
    out_content = read_file(out_path)
    compared_content_log = read_file('./snapshots/cat.log')
    compared_content_out = read_file('./snapshots/cat.out')

    assert log_content == compared_content_log
    assert out_content == compared_content_out
    print("----------------cat test success----------------")


def read_file(src: str) -> str:
    with open(src, 'r') as file:
        s = ''.join(file.readlines())
    return s


if __name__ == '__main__':
    test_cat()
