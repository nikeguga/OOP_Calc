# Калькулятор на Python

Этот проект представляет собой калькулятор на Python, созданный с использованием архитектурных паттернов, логирования и принципов SOLID.

## Как запустить

1. **Установите Python:** Убедитесь, что у вас установлен Python. Можно скачать его с [официального сайта Python](https://www.python.org/downloads/) и соответствующая IDE (Pychar, Spydr, VSCode etc.) В случае просмотра через VS Code - убедитесь в установке расширения для python
2. Скачайте/клонируйте репозиторий
3. Запустите файл main.py


## Принципы ООП:

1. **Инкапсуляция**: Классы (Calculator, Context, Addition, Multiplication, Division) инкапсулируют свою функциональность, предоставляя интерфейс для взаимодействия с внешним миром.

2. **Наследование**: Классы Addition, Multiplication, Division наследуют общую функциональность от базового класса Calculator. Это демонстрирует использование наследования для повторного использования кода.

3. **Полиморфизм**: Каждый класс операции реализует метод execute, что поддерживает полиморфизм. Это означает, что различные операции могут использоваться через общий интерфейс.

## Принципы SOLID:
1. **Принцип единственной ответственности (Single Responsibility Principle, SRP)**: Каждый класс отвечает за свою функциональность. Например, Calculator управляет базовой логикой калькулятора, Context управляет стратегиями, а классы операций выполняют конкретные операции.

2. **Принцип открытости/закрытости (Open/Closed Principle, OCP)**: Классы могут быть расширены для добавления новых операций без изменения существующего кода. Это достигается за счет использования стратегии для операций и создания новых классов операций при необходимости.

3. **Принцип подстановки Барбары Лисков (Liskov Substitution Principle, LSP)**: Классы операций могут быть использованы вместо базового класса Calculator, не нарушая функциональности программы.

4. **Принцип инверсии зависимостей (Dependency Inversion Principle, DIP)**: Класс Context зависит от абстракции (Calculator), а не от конкретных классов. Это позволяет легко вносить изменения и добавлять новые операции.