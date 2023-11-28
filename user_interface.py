class UserInterface:
    @staticmethod
    def get_operation():
        return input("Выберите операцию (+, *, /) или введите 'exit' для выхода: ").lower()

    @staticmethod
    def get_operands():
        try:
            operand1 = float(input("Введите первый операнд: "))
            operand2 = float(input("Введите второй операнд: "))
            return operand1, operand2
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return None, None
