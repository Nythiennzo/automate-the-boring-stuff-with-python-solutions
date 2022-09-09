try:
    raise Exception('This is an exception')
except Exception as exception:
    print(dir(exception))
    print(f'args: {type(exception.args)}')
    
    for index, arg in enumerate(exception.args):
        print(f'arg[{index}]: {type(arg)}')

    print(exception.args[0])