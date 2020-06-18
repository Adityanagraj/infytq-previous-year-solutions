""" 
Solve the problem based on the number of special characters.If the count is odd print 
first odd digits and next even digits(and viceversa) in the same series present in the string.

>>Input 1
  abc@147#25%gd&b
>>Output 1
  42175
>>Input 2
  fc#@23%34df
>>Output 2
  3324
"""

n=input()
even=[]
odd=[]
c=0
for i in n:
    if i.isalnum():
        c+=1
    if i.isdigit():
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
spl_char=len(n)-c
if spl_char%2!=0:
    sum=odd+even
    print(''.join(sum))
else:
    sum1=even+odd
    print(''.join(sum1))