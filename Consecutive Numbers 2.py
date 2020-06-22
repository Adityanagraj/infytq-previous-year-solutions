"""
Consider M*N matrix.If any num is consecutive for 3 times either in row , column, diagonals 
print the number.If there are multiple cases print the smallest of them.

>>Input 1
  4 5
  1 2 3 4 5
  6 7 8 9 0
  1 2 3 4 5
  6 7 8 9 0
>>Output 1
  -1
>>Input 2
  4 5
  1 2 3 4 5
  1 2 3 4 5
  1 2 3 4 5
  1 2 3 4 5 
>>Output 2
  1

"""
row,col=list(map(int,input().split(' ')))
mat=[]
list1=[]
for r in range((row)):
    row_numbers=list(map(int,input().split(' ')))
    mat.append(row_numbers)
for r in range((row)):
    for c in range((col)):
        if(c<col-2):
            if(mat[r][c]==mat[r][c+1]==mat[r][c+2]):
                list1.append(mat[r][c+1])
        if(r<row-2):
            if(mat[r][c]==mat[r+1][c]==mat[r+2][c]):
                list1.append(mat[r][c])
        if(r>=2 and c<col-2):
            if(mat[r][c]==mat[r-1][c+1]==mat[r-2][c+2]):
                list1.append(mat[r][c])
        if(r>=2 and c>=2):
            if(mat[r][c]==mat[r-1][c-1]==mat[r-2][c-2]):
                list1.append(mat[r][c])
if (len(list1)==0):
    print('-1')
else:
    print(min(list1))