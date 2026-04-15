from fraction import Fraction

def test_fraction_numerator_01():
    f = Fraction(3, 4)
    expected_numerator = 3
    actual_numerator = f.numerator
    assert expected_numerator == actual_numerator, f"Expected numerator {expected_numerator} but got {actual_numerator}"

def test_fraction_denominator_01():
    f = Fraction(3, 4)
    expected_denominator = 4
    actual_denominator = f.denominator
    assert expected_denominator == actual_denominator, f"Expected denominator {expected_denominator} but got {actual_denominator}"

def test_fraction_numerator_02():
    f = Fraction(3, 4)
    f.numerator = 5
    expected_numerator = 5
    actual_numerator = f.numerator
    assert expected_numerator == actual_numerator, f"Expected numerator {expected_numerator} but got {actual_numerator}"

def test_fraction_denominator_02():
    f = Fraction(3, 4)
    f.denominator = 5
    expected_denominator = 5
    actual_denominator = f.denominator
    assert expected_denominator == actual_denominator, f"Expected denominator {expected_denominator} but got {actual_denominator}"

def test_fraction_add():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = f1.add(f2)
    expected_numerator = 5
    expected_denominator = 4
    actual_numerator = f3.numerator
    actual_denominator = f3.denominator
    assert expected_numerator == actual_numerator, f"Expected numerator {expected_numerator} but got {actual_numerator}"
    assert expected_denominator == actual_denominator, f"Expected denominator {expected_denominator} but got {actual_denominator}"