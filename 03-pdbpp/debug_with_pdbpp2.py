def divide_numbers(a, b):
    return a / b

numbers = [10, 5, 0, 2]

for num in numbers:
    result = divide_numbers(100, num)
    print(f"100 / {num} = {result}")