#tuple DT

#Tuple is same as list where both is used to stroe the collection of data but the 
#The tuple is used to store the real constant values that it doesn't allows the updation or 
#deletion of value by 
#by using del operator we can delete the entire object of tuple but not specific obj
#list is MUTABLE and Tuple is IMMUTABLE
#list allow item assignment and updation but tuple not
#Tuple contans the index() and count() method we cant have all other methods from list
#by converting tuple to list we can perfrom all operations and convert back to tuple it is possible
#we can not convert fundamental values to tuple but byusing tuple([a]) like this we can do 
#we can perform  indexing and slicing on tulpelas well 
#

t=(10,2,4,3,6,7)
t2=sorted(t)
print(t2,type(t2))

t=t2
print(t[::-1])

tupl=(2,4,3,2,4,5,3,2,43,2,35,5,4,323,43,4)
print(tupl.count(2))
print(tupl.index(4))