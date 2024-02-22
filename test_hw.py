from main import prog


def test_hello_world() -> None:
    log_path = './devices/debug'
    out_path = './devices/output.out'

    prog('./devices/hello_world.asm',
         './devices/input.in',
         './devices/output.out')

    log_content = read_file(log_path)
    out_content = read_file(out_path)
    compared_content_log = read_file('./snapshots/hw.log')
    compared_content_out = read_file('./snapshots/hw.out')

    assert log_content == compared_content_log
    assert out_content == compared_content_out
    print("----------------hello world test success----------------")


def test_prob2() -> None:
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
    print("prob2 test success")


def test_wiyn() -> None:
    log_path = './devices/debug'
    out_path = './devices/output.out'

    prog('./devices/what_is_your_name.asm',
         './devices/input.in',
         './devices/output.out')

    log_content = read_file(log_path)
    out_content = read_file(out_path)
    compared_content_log = read_file('./snapshots/wiyn.log')
    compared_content_out = read_file('./snapshots/wiyn.out')

    assert log_content == compared_content_log
    assert out_content == compared_content_out
    print("what is your name test success")


def read_file(src: str) -> str:
    with open(src, 'r') as file:
        s = ''.join(file.readlines())
    return s


if __name__ == '__main__':
    test_hello_world()
