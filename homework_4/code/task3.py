import sys


def my_precious_logger(string):
    if string.startswith("error"):
        print(string, file=sys.stderr)
    else:
        print(string)


def test_my_precious_logger_positive(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK\n"
    assert captured.err == ""


test_my_precious_logger_positive()
