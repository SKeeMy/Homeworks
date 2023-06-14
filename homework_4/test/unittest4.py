import doctest
from tasks.homework_4.code.task3 import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(5) == ['1', '2', 'fizz', '4', 'buzz']
    assert fizzbuzz(15) == ['1', '2', 'fizz', '4', 'buzz', 'fizz',
                            '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']


doctest.testmod()
