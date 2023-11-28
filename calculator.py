class Calculator:
    def __init__(self):
        pass  # Дополнительная инициализация, если необходимо

    def execute_operation(self, strategy, operand1, operand2):
        return strategy.execute(operand1, operand2)

    # Дополнительные методы для ввода, вывода и других общих операций
    # ...


class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, operand1, operand2):
        if self.strategy:
            return self.strategy.execute(operand1, operand2)
        else:
            raise ValueError("Стратегия не установлена")
