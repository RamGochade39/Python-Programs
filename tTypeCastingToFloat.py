a=32
print(a,type(a))
b=float(a)
print(b,type(b))#32.0

a=45+5j
print(a,type(a))
b=float(a)
print(b,type(b))#Type error not possible 

a="33"
print(a,type(a))
b=float(a)
print(b,type(b))#33.0

a="33.43"
print(a,type(a))
b=float(a)
print(b,type(b))#possible 33.43

a="True"
print(a,type(a))
b=float(a)
print(b,type(b))#//value error

a=True
print(a,type(a))
b=float(a)
print(b,type(b))#1.o

a=False
print(a,type(a))
b=float(a)
print(b,type(b))#0.0
