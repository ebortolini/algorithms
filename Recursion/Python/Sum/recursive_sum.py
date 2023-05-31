def recursive_sum(numbers: list[int]) -> int:
    if numbers is None or len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    return numbers.pop(0) + sum(numbers)

