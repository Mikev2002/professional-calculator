# app/calculation/calculation.py

class Calculation:
    def __init__(self, a, b, operation_func):
        self.a = a
        self.b = b
        self.operation_func = operation_func
        self.result = self.operation_func(a, b)

    def get_result(self):
        return self.result
