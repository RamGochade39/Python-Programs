#the dict() is predefine class in python 
#the purpose of dict is to store k:v pair data the key cant't be duplicate if duplicate is given it 
#will override the previous value with nuw one 
#if we try to access like this d1[k] if key is not present the KeyError will come
#The dict is mutable  reserves insertion order
#indexing and slicing is not possible
#value can be changed but key can't  
d1={18:"virat",45:"rohit",7:"MSD",1:"KL Rahul"}
print(d1[18])
print(d1)

d1[333]="karun"
print(d1)

#clear all dict but keeps empty dict
d1.clear()

d1={18:"virat",45:"rohit",7:"MSD",1:"KL Rahul"}

#used to copy one dict to another
d2=d1.copy()
print(d2)

#used to remove kv pair based on key if key not present KeyError 
d1.pop(18)
print(d1)

#remove last kv pair if not KeyError
d1.popitem()

#it is used to get data based on key if not present None will be return
d1={18:"virat",45:"rohit",7:"MSD",1:"KL Rahul"}
print(d1.get(19))