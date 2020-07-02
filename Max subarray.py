"""
To find the max Subarray in the form of the x[i]=x[i-1]+x[i-2]
and print the elements in the list form

>>Input 
  3,5,8,2,19,12,7,17
>>Output
  2,3,5,8

"""
aa=list(map(int,input.split()))
aa=sorted(aa)
j=[]
j.append(aa[0])
j.append(aa[1])
for i in range(2,len(aa)):
	if j[i-1]+j[i-2] in aa:
		j.append(j[i-1]+j[i-2])
	else:
		break
print(j)