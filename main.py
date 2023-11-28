from calculator import Calculator, Context
from operations import Addition, Multiplication, Division
import logger  # предполагается, что у вас есть файл logger.py

def main():
    # Создаем экземпляр калькулятора
    calculator = Calculator()

    # Создаем экземпляр контекста для управления операциями
    context = Context()

    while True:
        # Получаем операцию от пользователя
        operation = input("Выберите операцию (+, *, /) или введите 'exit' для выхода: ").lower()

        # Проверяем, нужно ли выйти из программы
        if operation == 'exit':
            break

        # Устанавливаем соответствующую операцию стратегию в контексте
        if operation == '+':
            context.set_strategy(Addition())
        elif operation == '*':
            context.set_strategy(Multiplication())
        elif operation == '/':
            context.set_strategy(Division())
        else:
            print("Некорректная операция. Попробуйте еще раз.")
            continue

        try:
            # Получаем операнды от пользователя
            operand1 = float(input("Введите первый операнд: "))
            operand2 = float(input("Введите второй операнд: "))

            # Выполняем операцию
            result = context.execute_strategy(operand1, operand2)

            # Выводим результат
            print(f"Результат: {result}")

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль.")

if __name__ == "__main__":
    main()
