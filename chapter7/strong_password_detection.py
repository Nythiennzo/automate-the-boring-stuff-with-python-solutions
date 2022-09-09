import re

def is_strong_password(password):
    
    #length check
    if re.compile('.{8,}').search(password) == None:
        return False
    
    #upper case
    if re.compile('[A-Z]').search(password) == None:
        return False
    
    #lower case
    if re.compile('[a-z]').search(password) == None:
        return False

    #digit
    if re.compile('\d').search(password) == None:
        return False

    return True
    

print(is_strong_password(''))
print(is_strong_password('12345678'))
print(is_strong_password('abcdefgh'))
print(is_strong_password('ABCDEFGH'))
print(is_strong_password('123456zA'))
print(is_strong_password('1256zA'))
print(is_strong_password('abcd12A423'))