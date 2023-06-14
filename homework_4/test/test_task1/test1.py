import pytest

from code.task1_read_file import read_magic_number
import sys
sys.path.append(
    'C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/')


@pytest.mark.parametrize("path, expected_result", [('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/tests/test_task1/test_data1_yes.txt', True),
                                                   ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/tests/test_task1/test_data2_yes.txt', True)])
def test_read_magic_number_true(path, expected_result):
    """Tests whether read_magic_number returns the true when the first line of the file is a number in range interval [1, 3)*"""
    assert read_magic_number(path) == expected_result


@pytest.mark.parametrize("path, expected_result", [('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/tests/test_task1/test_data1_no.txt', False),
                                                   ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/tests/test_task1/test_data2_no.txt', False)])
def test_read_magic_number_false(path, expected_result):
    """Tests whether read_magic_number returns the false when the first line of the file is't a number in range interval [1, 3)*"""
    assert read_magic_number(path) == expected_result


@pytest.mark.parametrize("path, expected_error", [(2, ValueError),
                                                  ([2, 4], ValueError),
                                                  ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/tests/test_task1/error.txt', ValueError),
                                                  ('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/tests/testy_task1/test_data1_no.txt', ValueError),
                                                  ('D:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/tests/test_task1/test_data1_no.txt', ValueError)])
def test_read_magic_number_error(path, expected_error):
    """Tests whether read_magic_number throws a ValueError in case of any error"""
    with pytest.raises(expected_error):
        read_magic_number(path)


if __name__ == '__main__':
    pytest.main()
