"""
To form a 4 digit otp from a give number by selecting the elements from the odd positions 
from the given number

>>Input 1
  4365188
>>Output 1
  9256
>>Input 2
  543651
>>Output 2
  1636

""" 
x= str(input())
otp=''
for i in range(1,len(x)):
    if i%2!=0:
        otp+= str(int(x[i])**2) 
print(otp[0:4])
    