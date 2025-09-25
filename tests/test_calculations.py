from app.calculation.calculation import Calculation
from app.operation import operations

def test_add_calculation():
    calc = Calculation(3, 2, operations.add)
    assert calc.get_result() == 5

def test_subtract_calculation():
    calc = Calculation(5, 3, operations.subtract)
    assert calc.get_result() == 2

def test_multiply_calculation():
    calc = Calculation(4, 2, operations.multiply)
    assert calc.get_result() == 8

def test_divide_calculation():
    calc = Calculation(10, 2, operations.divide)
    assert calc.get_result() == 5
