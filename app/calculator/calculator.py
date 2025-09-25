# app/calculator/calculator.py

from app.calculation.calculation import Calculation

class Calculator:
    history = []

    @staticmethod
    def create_calculation(a, b, operation_func):
        calc = Calculation(a, b, operation_func)
        Calculator.history.append(calc)
        return calc

    @staticmethod
    def get_history():
        return Calculator.history

    @staticmethod
    def clear_history():
        Calculator.history.clear()
