"""
In which to find the the largest sum of matrix and print it in form of matrix 

>>Input 1
  0,3,6,12,3,6,-12,3,-3
>>Output 1
  0 3 
  12 3 

  0 3 6 
  12 3 6 
 -12 3 -3 

  3 6 
  3 6 
>>Input 2
  1,3,5,6,10
>>Output 2
  1 3 
  5 6 

"""
import math
def maxSum(matrix,rc,r,c,d):
    matrix_sum=0
    r2=r
    c2=c
    for i in range(d+1):
        for j in range(d+1):
            matrix_sum+=matrix[r2][c2]
            
            c2+=1
        r2+=1
        c2=c
    return matrix_sum
def printMatrix(matrix,rc,r,c,d,max_sum):
    matrix_sum=0
    r2=r
    c2=c
    sub_matrix=''
    for i in range(d+1):
        for j in range(d+1):
            matrix_sum+=matrix[r2][c2]
            sub_matrix+=str(matrix[r2][c2])+" "
            c2+=1
        r2+=1
        c2=c
      
        sub_matrix+='\n'
        if(matrix_sum==max_sum):
            print((sub_matrix))
    
        
lst_input = list(map(int,input().split(',')))
length=len(lst_input)
rc=int(math.sqrt(length))
matrix=[]
for i in range(0,length,rc):
    matrix.append(lst_input[i:rc+i])
max_sum=-1000000
for i in range(rc):
    for j in range(rc):
        for sqmt in range(rc):
            if(sqmt+i<rc and sqmt+j<rc):
                matrix_sum=maxSum(matrix,rc,i,j,sqmt)
            if(matrix_sum>max_sum):
                max_sum=matrix_sum
for i in range(rc):
        for j in range(rc):
            for sqmt in range(rc): 
                if(sqmt+i<rc and sqmt+j<rc):
                    printMatrix(matrix,rc,i,j,sqmt,max_sum)