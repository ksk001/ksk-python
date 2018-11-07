print("hi user, please enter the data")
x=float(input('x='))
y=float(input('y='))

z=x+y
print(z)
if z > 100:
    print('z is out of range ')
    print ( 'try another data')
while z>=100:
    x = float(input('x='))
    y = float(input('y='))
    z = x + y
    print(z)

    if z>100:
        print("z is out of range")
        print('try another data')

if z < 100:
    print('z lies in expected range')
    print ('now you are eligible for using the calculator')
    print ('choose the value of "a" as required')
    print(' a=1 for addition; a=2 for subtraction; a=3 for multiplication /n ')
    print('a=4 for division')
    a = 0
    while a<= 4:
        a = int(input('a='))
        if a == 1:
            x = float(input('x='))
            y = float(input('y='))
            z = x + y
            print(z)
        if a==2:
            x = float(input('x='))
            y = float(input('y='))
            z = x - y
            print(z)
        if a==3:
            x = float(input('x='))
            y = float(input('y='))
            z = x * y
            print(z)
        if a==4:
            x = float(input('x='))
            y = float(input('y='))
            z = x / y
            print(z)

    print(' Thank You For Using The Service')