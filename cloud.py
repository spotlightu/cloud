def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
           if num > max_num:
             max_num = num
    return max_num

def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def bubble_sort(numbers):
    sorted_list = numbers.copy()
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                 sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    return sorted_list

numbers = []
enter = input("Введите список чисел через запятую: ")
for num in enter.split(','):
        numbers.append(int(num.strip()))

even_numbers = get_even_numbers(numbers)
max_num = find_max(numbers)
min_num = find_min(numbers)
sorted_numbers = bubble_sort(numbers)

# Вывод результатов
print(f"Четные числа: {even_numbers}")
print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
print(f"Отсортированный список: {sorted_numbers}")