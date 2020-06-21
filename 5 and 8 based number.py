"""
Input integers are separated by comma(,).Form num1 by adding all the numbers except which are 
present in between 5 and 8. And num2 by concating numbers from 5 to 8.Then display the sum of num1 and num2.

>>Input 1
  3,2,6,5,1,4,8,9
>>Output 1
  5168
>>Input 2
  3,2,5,2,5,1,8,4
>>Output 2
  52527

"""


arr=list(map(int,input().split(',')))
sum1=sum(arr[:arr.index(5)])+sum(arr[arr.index(8)+1:])
sum2=arr[arr.index(5):arr.index(8)+1]
x=''
for i in sum2:
    x+=str(i)
print(sum1+int(x))