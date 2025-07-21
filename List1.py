lst=[2,3,4,5,6,7,8]
lst.append("ram")
print(lst)
print("===============================")
print(lst.index(2))#if obj is not present it will return ValueError
print("===============================")
lst.insert(0,"start")
lst.insert(len(lst),"end")
print(lst)
print("===============================")

print("===============================")
lst.insert(-234,0)
lst.insert(10000,100)
print(lst)
print("===============================")

print("===============================")
lst.remove("start")
#lst.remove("eend")#ValueError if object is not present
print(lst)
print("===============================")

print("===============================")
lst.pop(0)
#lst.pop(100)#IndexError if index is not present
print(lst)
print("===============================")

print(lst.clear())#remove all things but still it keeps the 
#[] empty and if we print that it will give you None output
lst.append("rma")
print(lst)

print("============================================")
del lst[2]
print(lst)