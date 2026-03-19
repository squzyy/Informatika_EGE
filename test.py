"""colors = ["красный", "зеленый", "синий"]

# Простой перебор
for color in colors:
    print(f"Цвет: {color}")

# Перебор с индексами
for i, color in enumerate(colors):
    print(f"{i+1}-й цвет: {color}")

# 1. Метод sort() - сортирует исходный список
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # [1, 2, 5, 8, 9]

# 2. Функция sorted() - создает новый отсортированный список
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 8, 9]
print(numbers)         # [5, 2, 8, 1, 9] - исходный не изменился"""

"""fruits = sorted(['dobley', 'apple'])
print(fruits)"""
def process_number(n):
    # Получаем двоичную запись числа (без префикса '0b')
    binary = bin(n)[2:]
    
    # Проверяем, кратно ли число 3
    if n % 3 == 0:
        # Получаем три младших разряда (последние 3 символа)
        three_low_bits = binary[-3:] if len(binary) >= 3 else binary
        # Дописываем их в конец
        binary += three_low_bits
    
    return binary

# Пример использования
number = 21  # 21 кратно 3 (21 = 3 * 7)
result = process_number(number)
print(f"Исходное число: {number}")
print(f"Двоичная запись: {bin(number)[2:]}")
print(f"Результат: {result}")