lst=[2,3,4,5,2,4,5,3,6,7,8]
print("============Enumerate used to take index + values=====================")
for i,v in enumerate(lst):
    print(i,"===>",v)

print("================The copy method perform shallow copy of list=================")
lst2=lst.copy();
print(lst,id(lst))
print(lst2,id(lst2))

print("================To perform Deep Copy we use '=' =================")
lst2=lst
print(lst,id(lst))
print(lst2,id(lst2))

print("==========count is used to count the frequency of provided object in list===========")
lst=[2,3,4,5,2,4,5,3,6,7,8]
count=lst.count(2)#if given valuee is not present it will return 0 count
print(count)

print("==========reverse()  is used to reverse the list ===========")
lst=[2,3,4,5,2,4,5,3,6,7,8]
lst.reverse()
print(lst)

print("==========sort is used to perform sorting of list ===========")
lst=[2,3,4,5,2,4,5,3,6,7,8]
lst.sort()#by default it sort in asc order to make it desc we use sort(reverse=true)
lst.sort(reverse=True)
print(lst)

print("================extend() is used to merge to lists========================")
lst1=[1,2,3]
lst2=[4,5,6]
#lst1.extend(lst2)
lst1=lst1+lst2#this is also merging but memory location will be different
print(lst1)