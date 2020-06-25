"""
In this program given a string join the words based on similar char in combinations
then concatinate the first and last element alternatively

>>Input 1
  heLloOWorLDd
>>Output 1
  DdWerhoOoLlL
>>Input 2
  GiTHub
>>Output 2
  buGTHi

"""
s = input()
l = sorted(set(s.upper()))
print((l))
res=[]
for i in range(len(l)):
    newstr=""
    for j in s:
        if(l[i]==j.upper()):
            newstr+=j 
    res.append(newstr)
i=0
j=len(res)-1
out=""
while i<=j:
    if i==j:
        out+=res[i]
    else:
        out+=res[i]+res[j]
    i+=1
    j-=1
print(out)    
