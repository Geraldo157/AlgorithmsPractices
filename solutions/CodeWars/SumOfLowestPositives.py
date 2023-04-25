def sum_two_smallest_numbers(numbers):
    num1 = min(numbers)
    numbers.pop(numbers.index(num1))
    total = num1 + min(numbers)
    return total
