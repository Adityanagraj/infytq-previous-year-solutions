"""
To check whether the given bracket is balanced or not if balanced return 0 else return the position where it is 
breaking in the form of count

>>Input 1
  []
>>Output 1
  0
>>Input 2
  {{[[}}
>>Output 2
  5

"""
def par(x):
    stack=[]
    count=0
    for i in x:
        if i in ['[','{','(']:
            stack.append(i)
            count+=1
            continue
        if (len(stack)==0):
            return count+1
        y=stack.pop()
        if (i==']'and y=='['):
            count+=1
        elif (i=='}'and y=='{'):
            count+=1
        elif (i==')'and y=='('):
            count+=1
        else:
            return count+1
    if (len(stack)==0):
        return 0
    else:
        return count+1
x=input()
print(par(x))
