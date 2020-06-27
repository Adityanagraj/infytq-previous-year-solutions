"""
Find the factors of given number and see it is present in the the given set of factors
if it is present the list print the elements in the list if no element found print -1
 
>>Input 1
  1,2,4,7
>>Output 1
  [1, 4]
>>Input 2
  2,5,4,8
>>Output 2
  -1

"""
def findfactsum(n):
        s=1
        for j in range(2,n+1):
            if n%j==0:
                s+=j 
        return s        
res=[]
m=-1
l=list(map(int,input().split(',')))
for i in l:
    val=findfactsum(i)
    if val in l:
        res.append(i)
if(len(res)==0):

    print(m)
else:
    print(sorted(res))

