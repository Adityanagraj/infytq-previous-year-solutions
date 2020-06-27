"""
To find the longest unique substring in the given input string and print the length of unique
charaters if no such string is found return -1

>>Input 1
  abbcdb
>>Output 1
  3
>>Input 2
  aaaa
>>Output 2
  -1
"""
string=input()
length=len(string)
u=''
for i in range(length):
    sub=string[i]
    for j in range(i+1,length):
        sub+=string[j]
        sub_len=len(sub)
        if(sub_len>=3 and len(set(sub))==sub_len):
            if(len(u)<sub_len):
                u=sub
if(len(u)==0):
    print('-1')
else:
    print(len(u))