"""
Find the number of distinct odd subarrays in list,such that the sum of the subarray is an odd integer. 
Two subarray are considered to be different if they either start or end at different index.

>>Input 1
  1 2 3
>>Output 1
  1
  1 2
  2 3
  3
>>Input 2
  1 3 5 7
>>Output 2
  1
  1 2
  2 3
  2 3 4
  3
  3 4

"""
n1=list(map(int,input().split(' ')))
a=[]
for i in range(1,len(n1)+1):
    a.append(i)
ll=[a[i:j+1] for i in range(len(a)) for j in range(i,len(a))]
length=(len(ll))
m=-1
c=0
count=0
list1=[]
for i in ll:
    if sum(i)%2!=0:
        c+=1
        list1.append(i)
for i in ll:
    if sum(i)%2==0:
        count+=1
if count==length:
    print(m)
for i in list1:
    print(' '.join(list(map(str, i))))