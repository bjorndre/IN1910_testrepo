from calculator import add, factorial, divide, sin, exponential, multiplication
from pytest import approx, raises, mark
import math as m

@mark.parametrize(
    "arg, expected", [[(1,2), 3], [(8, 15), 23], [(-4, -2), -6]]
)
def test_add_exercise_1(arg, expected):
    assert add(arg[0], arg[1]) == expected

@mark.parametrize(
    "arg, expected", \
        [[(0.1,0.2), 0.3], [(0.08, 0.15), 0.23], [(-0.4, -0.2), -0.6]]
)
def test_add_exercise_2(arg, expected):
    allowed_error = 0.00001
    assert approx(add(arg[0],arg[1]), expected, abs=allowed_error)

@mark.parametrize(
    "arg, expected", [[("Hello ","World"), "Hello World"], \
        [("Det bor en baker ", "i Østre Aker"), \
        "Det bor en baker i Østre Aker"], \
        [("Play Fire Emblem ", "Thracia 776"), "Play Fire Emblem Thracia 776"]]
)
def test_add_exercise_3(arg, expected):
    assert add(arg[0], arg[1]) == expected

@mark.parametrize(
    "arg, expected", [(5, m.factorial(5)), (0, m.factorial(1)), \
        (12, m.factorial(12))]
)
def test_factorial_exercise_4(arg, expected):
    assert factorial(arg) == expected

@mark.parametrize(
    "arg, expected", [((4, 10), m.sin(4)), ((0, 10), m.sin(0)), \
        ((-5, 100), m.sin(-5))]
)
def test_sin_exercise_4(arg, expected):
    allowed_error = 0.00001
    assert approx(sin(arg[0],arg[1]), expected, abs=allowed_error)

@mark.parametrize(
    "arg, expected", [((10, 2), 5), ((-10, 2), -5), ((-20, -5), 4)]
)
def test_divide_exercise_4(arg, expected):
    assert divide(arg[0], arg[1]) == expected

@mark.parametrize(
    "arg, expected", [((3,4), 81), ((4,0), 1), ((-3,3), -27)]
)
def test_exponential_exercise_4(arg, expected):
    assert exponential(arg[0], arg[1]) == expected

@mark.parametrize(
    "arg, expected", [((5,3), 15), ((-5,3), -15), ((0,3), 0)]
)
def test_multiplication_exercise_4(arg, expected):
    assert multiplication(arg[0], arg[1]) == expected

@mark.parametrize(
    "arg", [("Potet", 18), (0.5, "Høner"), ("Thracia", 776)]
)
def test_add_with_string_and_number_exercise_5(arg):
    with raises(TypeError):
        add(arg[0], arg[1])

@mark.parametrize(
    "arg", [(15, 0), (-3, 0), (0, 0)]
)
def test_if_divide_raises_ZeroDivisonError_when_dividing_by_zero_exercise_5(arg):
    with raises(ZeroDivisionError):
        divide(arg[0], arg[1])