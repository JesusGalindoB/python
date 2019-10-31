def binary_array_to_number(arr:list) -> int:
    return sum(2** index for index, value in enumerate(reversed(arr)) if value == 1)  