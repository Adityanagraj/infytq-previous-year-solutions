"""
A non empty string containing only alphabets. Print length of longest prefix in the string 
which is same as suffix without overlapping.Else print -1 if no prefix or suffix exists.

>>Input 1
  Racecar
>>Output 1
  -1
>>Input 2
  aaaa
>>Output 2
  2
"""
string=input()
length=len(string)
mid=int(length)//2
m=-1
for i in range(mid,0,-1):
    pre=string[0:i]
    suf=string[length-i:length]
    if (pre==suf):
        print(len(suf))
        break
else:
    print(m)