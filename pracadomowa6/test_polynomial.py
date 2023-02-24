from Polynomial import Polynomial
from pytest import raises


def test_constructor_not_empty():
    polynomial = Polynomial([(0, 4), (1, -2)])
    assert polynomial._polynomial_parameters == {0: 4, 1: -2}


def test_constructor_empty():
    polynomial = Polynomial()
    assert polynomial._polynomial_parameters == {}


def test_constructor_negative_degree():
    with raises(ValueError):
        Polynomial([(1, 5), (-3, 7), (5, -1)])


def test_constructor_zero_factor():
    with raises(ValueError):
        Polynomial([(1, 5), (3, 0), (5, -1)])


def test_constructor_repeated():
    with raises(ValueError):
        Polynomial([(1, 5), (3, 0), (1, 7)])


def test_set_parameters_negative_power():
    polynomial = Polynomial([(0, 4), (1, -2)])
    with raises(ValueError):
        polynomial.set_parameters(-1,2)


def test_set_parameters_add_to_existing_power():
    polynomial = Polynomial([(0, 4), (1, -2)])
    with raises(ValueError):
        polynomial.set_parameters(0,2)

def test_str():
    polynomial = Polynomial([(0, 4), (1, -2)])
    assert str(polynomial) == '-2x+4'


def test_str_negative_1_on_start():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert str(polynomial) == '-x^5+2x^3+5x'


def test_str_1_on_start():
    polynomial = Polynomial([(4, 2), (6, 1), (2, 3), (0, 7)])
    assert str(polynomial) == 'x^6+2x^4+3x^2+7'


def test_str_1_on_end():
    polynomial = Polynomial([(1, 5), (0, 1)])
    assert str(polynomial) == '5x+1'


def test_str_negative_1_on_end():
    polynomial = Polynomial([(1, 5), (0, -1)])
    assert str(polynomial) == '5x-1'


def test_str_power_1_and_factor_1():
    polynomial = Polynomial([(1, 1), (0, -1)])
    assert str(polynomial) == 'x-1'

def test_empty_str():
    polynomial = Polynomial()
    assert str(polynomial) == ''


def test_str_one_number():
    polynomial = Polynomial([(0, 5)])
    assert str(polynomial) == '5'


def test_degree():
    polynomial = Polynomial([(0, 4), (1, -2)])
    assert polynomial.degree() == 1


def test_degree_empty():
    polynomial = Polynomial()
    assert polynomial.degree() == None


def test_coefficient():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert polynomial.coefficient(5) == -1


def test_coefficient_doesnt_exist():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert polynomial.coefficient(4) == 0



def test_value():
    polynomial = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert polynomial.value(2) == 10 + 16 - 32


def test_value_zero():
    polynomial = Polynomial([(0, 4), (1, -2)])
    assert polynomial.value(0) == 4


def test_value_very_great():
    polynomial = Polynomial([(7, 2), (5, 3), (2, 3), (0, -5)])
    assert polynomial.value(6) == 559872 + 23328 + 108 - 5


def test_add():
    poly1 = Polynomial([(0, 4), (1, -2)])
    poly2 = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert str(poly1+poly2) == '-x^5+2x^3+3x+4'


def test_add_2():
    poly1 = Polynomial([(7, 2), (3, 3), (2, 3), (0, -5)])
    poly2 = Polynomial([(5, 3), (3, -3)])
    assert str(poly1 + poly2) == '2x^7+3x^5+3x^2-5'


def test_subtract():
    poly1 = Polynomial([(7, 2), (5, 3), (2, 3), (0, -5)])
    poly2 = Polynomial([(5, 3), (3, -3)])
    assert str(poly1 - poly2) == '2x^7+3x^3+3x^2-5'



def test_subtract_2():
    poly1 = Polynomial([(0, 4), (1, -2)])
    poly2 = Polynomial([(1, 5), (3, 2), (5, -1)])
    assert str( poly1 - poly2) == 'x^5-2x^3-7x+4'