import re
from typing import Callable, Generator

# Функция для генерации чисел из текста
def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r'\b\d+\.\d+|\b\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

# Функция для суммирования чисел, полученных из текста
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    
    return sum(func(text))

# Пример использования
if __name__ == "__main__":
    text = "Общий доход работника состоит из нескольких частей: 1000.01 как основной доход, дополненный дополнительными поступлениями 27.45 и 324.00 долларов."
    total_income = sum_profit(text, generator_numbers)
    print(f"Общий доход: {total_income}")