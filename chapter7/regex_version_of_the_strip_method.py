import re


import re

def my_strip(input_string, sub_string=''):
    return re.compile('^\s+|\s+$').sub(sub_string, input_string)


def test_my_strip(input_string, sub_string=''):
    print("Before my Strip '" + input_string + "' have a lengt of " + str(len(input_string)))
    result = my_strip(input_string, sub_string)
    print("After my Strip '" + result + "' have a lengt of " + str(len(result)))
    print()


test_my_strip('this is my test string')
test_my_strip('   this is my test string')
test_my_strip('this is my test string    ')
test_my_strip('   this is my test string    ')
    
test_my_strip('this is my test string', '*')
test_my_strip('   this is my test string', '*')
test_my_strip('this is my test string    ', '*')
test_my_strip('   this is my test string    ', '*')
