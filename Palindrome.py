#Write a program that checks if a given number is a palindrome (reads the same forwards and
#backwards) using a while loop
n=int(input('Enter a number: '))
r=0
s=0
check=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if check==s:
    print('Palindrome')
else:
    print('Not Palindrome')