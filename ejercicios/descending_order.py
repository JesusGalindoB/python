def descending_order(num):
    if num >= 0:
        num_string = str(num)
        new_list = []
        new_string = ""
        for value in num_string:
            conversion = int(value)
            new_list.append(conversion)
            new_list.sort(reverse=True)
        for element in new_list:
            new_string = new_string + str(element)
        new_num = int(new_string)
    return new_num

result = Descending_Order(145263)
print(result)

