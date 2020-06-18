"""
Reverse the given input string without changing the positions of the special characters.

>>Input 1
  abcd@12#ef$k
>>Output 1
  abcd@12#ef$k

>>Input 2
  a@%3e4#y
>>Output 2
  y@%4e3#a
"""

s=input()
d=dict()
res=''
for i in range(len(s)):
    if s[i].isalnum()==False:
        d.update({i:s[i]})
    else:
        res+=s[i]
res=list(res[::-1])
for i,j in d.items():
    res.insert(i,j)
print(''.join(res))
