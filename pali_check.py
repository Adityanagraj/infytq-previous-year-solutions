"""
To check the given number is palindrome if not add the number to the result
and provide the length of the palindrome

>>Input 1
  1234
>>Output 1
  4
>>Input 2
  123
>>Output 2
  3

"""
def palicheck(num):
    x=num[::-1]
    if x==num:
        return True
    return False
n=input()
val=0
sum=0
while(True):
    if (palicheck(n)):
        val=len(n)
        print(val)
        break
    
    else:
        s1=n[::-1]
        sum=int(n)+int(s1)
        n=str(sum)
        palicheck(n)