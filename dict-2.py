d1={18:"virat",45:"rohit",99:"sumit",23:"suresh"}
#get is get the specfic valued from key but key not present None 
print(d1.get(18))

#items() gives kv pair in tuple
for k in d1.items():
    print(k)

#keys() will give you all keys
for k in d1.keys():
    print(k)

#values() will give you all values
for k in d1.values():
    print(k)

