"""
In this program we find various possible combinations of all the given numbers 
and form a special sum from it

>>Input 1
  -1,1,0,0,2,-2
>>Output 1
  3

"""
import itertools
x=list(map(int,input().split(',')))
y=int(input())
res=list(itertools.combinations(x,4))
c=0
for i in res:
	u=sum(i)
	if u==y:
		c+=1
print(c)