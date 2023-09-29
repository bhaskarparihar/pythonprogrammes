import random
a=random.randrange(1,101)
while True:
    b=int(input("Enter a number:- "))
    if  b==a:
        print('You win')
        break
    elif b<a:
        print('Small')
    else:
        print('Large')
