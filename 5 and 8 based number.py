"""

"""


arr=list(map(int,input().split(',')))
sum1=sum(arr[:arr.index(5)])+sum(arr[arr.index(8)+1:])
sum2=arr[arr.index(5):arr.index(8)+1]
x=''
for i in sum2:
    x+=str(i)
print(sum1+int(x))