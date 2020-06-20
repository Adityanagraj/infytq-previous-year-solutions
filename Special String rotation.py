"""
Every string is associated with the number separated by colon(:).Task is to rotate the string based on the number. 
If the sum of square of digits is even then rotate the string right by 1 position else rotate the string left 
by 2 position.

>>Input 1
  rhdt:246,ghftd:1246
>>Output 1
  trhd ftdgh
>>Input 2
  abcd:1234,bcdgfhf:127836,sdjks:1245
>>Output2
  dabc dgfhfbc ssdjk 
"""
dicti=input().split(',')
for obj in dicti:
    str_obj=obj.split(':')
    string=str_obj[0]
    length=len(string)
    num=str_obj[1]
    sum1=0
    for digit in num:
        sum1+=(int(digit)**2)
    if sum1%2==0:
        s=string[length-1:length]
        print(s+string[0:length-1],end=' ')
    else:
        s=string[0:2]
        print(string[2:length]+s,end=' ')