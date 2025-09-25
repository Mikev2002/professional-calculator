from app.calculator.calculator import Calculator
from app.operation import operations

def test_create_add_calculation():
    Calculator.clear_history()
    calc = Calculator.create_calculation(3, 2, operations.add)
    assert calc.get_result() == 5
    assert len(Calculator.get_history()) == 1

def test_create_subtract_calculation():
    Calculator.clear_history()
    calc = Calculator.create_calculation(10, 4, operations.subtract)
    assert calc.get_result() == 6

def test_history_contains_calculation():
    Calculator.clear_history()
    calc = Calculator.create_calculation(5, 5, operations.multiply)
    history = Calculator.get_history()
    assert len(history) == 1
    assert history[0].get_result() == 25

def test_clear_history():
    Calculator.create_calculation(1, 1, operations.add)
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0
