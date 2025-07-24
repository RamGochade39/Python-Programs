#most frequncy digit in list

lst=[2,2,1,3,1,2,2,3]

print(lst)
fqr=0;
digit=0
for i in lst:
    c=lst.count(i)
    if(c>fqr):
        fqr=c;
        digit=i;

print(digit ,"===========>",fqr)