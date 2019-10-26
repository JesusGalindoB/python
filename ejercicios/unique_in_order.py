def unique_in_order(iterable):
    new = []
    value = None
    for element in iterable:
        if element != value:
            value = element
            new.append(value)
    return new


def item_not_repeated(iterable):
    new = []
    for element in iterable:
        value = element in new
        if value == False:
            new.append(element)
    return new

iterable = ([1, 2, 2, 3, 3])
result = unique_in_order(iterable)
print(result)