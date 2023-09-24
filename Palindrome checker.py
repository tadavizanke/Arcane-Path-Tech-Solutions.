user=input('enter a string:')
a= user[::1]
b= user[::-1]
if a==b:
    print('palindrome')
else:
    print('Not a palindrome')
