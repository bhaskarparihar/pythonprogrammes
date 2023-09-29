#Write a program that checks if a given number is prime or not using a while loop.
a=int(input('Enter a number: '))
c=1

while c<a:
    c+=1
    if a%c==0:
        print('Not prime')