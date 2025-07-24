#Set is predefine class and it used to store homo or hetrogenous data .
#set is mutable and immutable both it doest allow item assignment but it allows the adding or deleting 
#elements from set by using its own mwthods add() remove()
#indexing / slicing is not possible 
#it doesn't priserve order of insertion
#Set in set is not posible 
#list in set is not allowed 
#tuple in set is possible
#set in tuple is possible
#set in list is possible
#
#

s1={1,2,3,4,5,6,7}
print(s1,type(s1))
#used for adding element to set
s1.add(8);

#used to remove value from set based on passed value if value is not present KeyError
s1.remove(1)
print(s1)

#used to copy on e set obj to another shallow copy will be done
s2=s1.copy()
print(s2)

#pop() remove random value if it is not printed if printed 
# it will remove first value if set is null KeyError
s1.pop()


#it is also used to remove value from set but if not preset return None 
print(s1.discard(93))

#return false even if one element it both set is equal
print(s1.isdisjoint(s2))

#checks is s1 is subset of s2
print(s1.issubset(s2))

#checks is s1 is superset of s2
print(s1.issuperset(s2))


#this will add both the set values in on different set and removes duplicates
s1={1,2,7,8,9}
s2={1,2,3,4,5,6}
s3=s1.union(s2)
print(s3)

#takes only similar elements from both the set
s3=s1.intersection(s2)
print(s3)

#the diffence will give all uniques value of set one that is not in set 2

s3=s1.difference(s2)
print(s3)

#the s1 will take all unique value from s2 and add in s1
s1.update(s2)
print(s1)

