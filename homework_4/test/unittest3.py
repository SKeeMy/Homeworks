def test_my_precious_logger_positive(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.out == "OK\n"
    assert captured.err == ""
