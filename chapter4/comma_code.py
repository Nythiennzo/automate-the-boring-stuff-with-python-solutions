def comma_code(input_list):
    return_string = ''

    for index, item in enumerate(input_list):
        if index == 0 or len(input_list) == 1:
            return_string += item
        elif index == len(input_list) -1:
            return_string = return_string + ' and ' + item
        else:
            return_string = return_string + ', ' + item

    return return_string


print(comma_code([]))
print(comma_code(['item1']))
print(comma_code(['item1', 'item2']))
print(comma_code(['item1', 'item2', 'item3']))
print(comma_code(['item1', 'item2', 'item3', 'item4']))

