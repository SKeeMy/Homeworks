class Supressor:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, traceback):
        return exc_type is not None and issubclass(exc_type, self.exceptions)


from contextlib import contextmanager

@contextmanager
def suppressor_gen(*exceptions):
    try:
        yield
    except exceptions:
        pass


""" Tests """

def test_supressor():
    with Supressor(IndexError, ZeroDivisionError):
        assert [][2]

    print('Success')

def test_suprssor_gen():
    with suppressor_gen(IndexError, ZeroDivisionError):
        assert [][2]

    print('Success')

if __name__ == '__main__':
    test_supressor()
    test_suprssor_gen()