from mylib import add, divide

def test_add_01():
    a = 3
    b = 5
    expected = 8
    actual = add(a, b)
    assert expected == actual, f"Expected {expected} but got {actual}"

def test_add_02():
    a = 3
    b = 0
    expected = 3
    actual = add(a, b)
    assert expected == actual, f"Expected {expected} but got {actual}"

def test_add_03():
    a = 0
    b = 3
    expected = 3
    actual = add(a, b)
    assert expected == actual, f"Expected {expected} but got {actual}"

def test_divide_01():
    a = 10
    b = 2
    expected = 5
    actual = divide(a, b)
    assert expected == actual, f"Expected {expected} but got {actual}"
    assert isinstance(actual, float), f"Expected type float but got {type(actual)}"

def test_divide_02():
    try:
        a = 10
        b = 0
        divide(a, b)
        assert False, "Expected ZeroDivisionError but no exception was raised"
    except ZeroDivisionError:
        assert False, "Expected ValueError but got ZeroDivisionError"
    except ValueError:
        pass