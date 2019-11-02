def zeros(n):
    division_one, division_two = n, n
    result_one, result_two = 0, 0 
    result = 0

    while division_one >= 2:
        division_one = division_one // 2
        result_one = result_one + division_one

    while division_two >= 5:
        division_two = division_two // 5
        result_two = result_two + division_two

    if result_two < result_one:
        result = result_two
    else:
        result = result_one
    return result
