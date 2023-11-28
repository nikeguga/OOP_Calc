from calculator import Calculator, Context
from operations import Addition, Multiplication, Division
from user_interface import UserInterface
import logger

def main():
    calculator = Calculator()
    context = Context()
    user_interface = UserInterface()

    while True:
        operation = user_interface.get_operation()

        if operation == 'exit':
            break

        if operation in ('+', '*', '/'):
            context.set_strategy(Addition() if operation == '+' else Multiplication() if operation == '*' else Division())
        else:
            print("Некорректная операция. Попробуйте еще раз.")
            continue

        operand1, operand2 = user_interface.get_operands()
        if operand1 is None or operand2 is None:
            continue

        try:
            result = context.execute_strategy(operand1, operand2)
            print(f"Результат: {result}")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()