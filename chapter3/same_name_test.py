box = 'global'

def func1():
    box = 'local'
    print(box)

def func2():
    print(box)
    #box = box + '+' #ERROR!
    #print(box)

def func3():
    global box
    print(box)
    box = box + '+'
    print(box)

print(box)
func1()
print(box)
func2()
print(box)
func3()
print(box)