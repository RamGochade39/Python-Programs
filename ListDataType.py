print("All About List Data Type")
#A list is predifine class in python 
#The purpose of list is to store the tht can be homogenous or heterogenous data
#We can perform indexing and slicing on it 
#we can convert the other data types values to list we do use list() 
#we cant pass the fundamental data types to list directly list(10) => wrong
#to conver the fundamental dt in list we can do something like list([23]) => right
#list is mutable dt means we can perform item assignment on it
lst=[34,53,3,234,34,"ram",54.5];
print(lst)

print(lst[0])
print(lst[0:4])
print(lst[1:7:2])

lst2=[]
print(lst2)

lst2=list()
print(lst2)

lst[0:3]=[12,32,5]

print(lst)

lst.append("sumit")
print(lst)