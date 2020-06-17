"""
Given input of array of string in format : separated by comas (,).Emp will contain only 
alphabets and employee number. You have to generate password based on input.

>> Input 1
   Robert:36787,Tina:68721,Jo:56389
>> Output 1
   tiX
>> Input 2
   abhishek:34848,Mayur:4739
>> Output 2
   Ku
"""
string=input()
final=''
list_input=[]
list_input=string.split(',')
for i in list_input:
    temp=i.split(':')
    name=temp[0]
    num=temp[1]
    length=len(name)
    max1=0
    for d in num:
        if(int(d)<=length):
            if(max1<int(d)):
                max1=int(d)
    if (max1==0):
        final+='X'
    else:
        final+=name[max1-1]
print(final)