a=32.6
print(a,type(a))
b=int(a)
print(b,type(b))#32

a=45+5j
print(a,type(a))
b=int(b)
print(b,type(b))#Type error not possible 

a="33"
print(a,type(a))
b=int(a)
print(b,type(b))#33

a="33.43"
print(a,type(a))
b=int(a)
print(b,type(b))#Not Possioble value error

a="True"
print(a,type(a))
b=int(a)
print(b,type(b))#//value error

a=True
print(a,type(a))
b=int(a)
print(b,type(b))#1

a=False
print(a,type(a))
b=int(a)
print(b,type(b))#0
