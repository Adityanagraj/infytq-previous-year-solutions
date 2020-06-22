"""
Find the all possible 2*2 matrix whose each element should be divisible by sum of its digits.

>>Input 1
  3
  42 54 2
  30 24 27 
  180 190 40
>>Output 1
  42 54
  30 24
  54 2
  24 27
  30 24
  180 190
  24 27
  190 40

"""
def divisible(n):
    x=sum(list(map(int,str(n))))
    if n%x==0:
        return True
    else:
        return False
mat=[]
n=int(input())
for i in range(n):
    x=(list(map(int,input().split())))
    mat.append(x)
col=len(mat[1])
for r in range(n-1):
    for c in range(col-1):
        if(divisible(mat[r][c]) and divisible(mat[r][c+1]) and divisible(mat[r+1][c]) and divisible(mat[r+1][c+1])):
            print(mat[r][c],mat[r][c+1])
            print(mat[r+1][c],mat[r+1][c+1])
