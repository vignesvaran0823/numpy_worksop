# find if the given number is a palindrome or not?
a=int(input( "Enter the first number: ")) 
if a==a[::-1]:
  print('given no is palindrome')
else:
  print('given no is not palindrome')
