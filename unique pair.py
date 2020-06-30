"""
find the unique no of pairs in the given list

>>Input 1
  34,89,6,321,53,45,2211,81
>>Output 1
  4
"""

import math
list_num=input().split(',')
digit_sum_list=[]
for num in list_num:
    digit_sum=sum(list(map(int,num)))
    digit_sum_list.append(digit_sum)
max_sum=max(digit_sum_list)
list_count=[0]*(max_sum+1)
for num in digit_sum_list:
    list_count[num]+=1
total=0
for count in list_count:
    if(count>1):
        total+=int(math.factorial(count)/(math.factorial(count-2)*2))
if(total==0):
    print('-1')
else:
    print(total)