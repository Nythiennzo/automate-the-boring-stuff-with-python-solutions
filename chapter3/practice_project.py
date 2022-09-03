def collatz(number):
    if number % 2 == 0:
       next_number =  int(number / 2)
    else:
        next_number = 3 * number + 1
    
    print(next_number)
    return next_number

number = None
while number == None:
    try:
        number = int(input('Number: '))
    except:
        print('Input was not an integer. Try again!')

while number != 1:
    number = collatz(number)