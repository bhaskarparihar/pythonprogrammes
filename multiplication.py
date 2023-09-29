#Create a program that takes an integer as input and prints the multiplication table for that number
#from 1 to 10 using a while loop.
a=int(input('Enter a number: '))
b=1
while  b<=10:
    c=a*b
    print(a,'*',b,'=',c)
    b+=1