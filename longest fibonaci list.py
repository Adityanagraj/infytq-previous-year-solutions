"""
To find the longest series of  finbonaci number in the given numbers and print the longest formed 
list from the above 

>>Input 1
  1,2,3,4,5,6
>>Output 1
  [1, 2, 3, 5]
>>Input 2
  1,2,5,8
>>Output 2
  -1

"""
list_number=list(map(int,input().split(',')))
length=len(list_number)
list_total=[]
for i in range(0,length):
    for x in range(i+1,length):
        first=list_number[i]
        second=list_number[x]
        fab_list=[]
        fab_list.append(first)
        fab_list.append(second)
        for y in range(x+1,length):
            if(first+second==list_number[y]):
                fab_list.append(list_number[y])
                first=second
                second=list_number[y]
        if(len(list_total)<len(fab_list)):
            list_total=fab_list
if(len(list_total)>2):
    print(list_total)
else:
    print('-1')