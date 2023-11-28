class Addition:
    def execute(self, operand1, operand2):
        return operand1 + operand2


class Multiplication:
    def execute(self, operand1, operand2):
        return operand1 * operand2


class Division:
    def execute(self, operand1, operand2):
        if operand2 == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")
        return operand1 / operand2
