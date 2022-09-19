def printer(x,y,z):
    print (str(x)+z+str(y))
def calculate():
    x=float(input("input x: "))
    y=float(input("input y: "))
    Operater = input("Operater: ")
    if Operater == 'add':
        printer(x,y,'+')
        print(round(x+y,2))
    elif Operater == 'subtract':
        printer(x,y,'-')
        print(round(x-y,2))
    elif Operater == 'multiply':
        printer(x,y,'*')
        print(round(x*y,2))
    elif Operater == 'divide':
        printer(x,y,'/')
        print(round(x/y,2))
    elif Operater == 'power':
        printer(x,y,'^')
        print(round(x**y,2))
calculate()