"""
The program is to find the next palindrome for the given number if the given number is palindrome 
return the number else calulate the next number and return the number

>>Input 1
  122
>>Output 1
  131
>>Input 2
  222
>>Output 2
  222

"""
def next_palindrome(x):
    while True:
        rev=int(str(x)[::-1])
        if rev==x:
            return x
        x+=1
x=int(input())
next_palindrome(x)