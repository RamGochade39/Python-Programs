a=32.6
print(a,type(a))
b=bool(a)
print(b,type(b))#True

# only 0 in int and 0.0 in float are fasle  and all the characters in 
# string without 0 length are true 

a=45+5j
print(a,type(a))
b=bool(a)
print(b,type(b))#True

a="33"
print(a,type(a))
b=bool(a)
print(b,type(b))#True

a="33.43"
print(a,type(a))
b=bool(a)
print(b,type(b))#True

a="True"
print(a,type(a))
b=bool(a)
print(b,type(b))#//true

a="False"
print(a,type(a))
b=bool(a)
print(b,type(b))#True

a=0
print(a,type(a))
b=bool(a)
print(b,type(b))#False

a=0.0
print(a,type(a))
b=bool(a)
print(b,type(b))#False

a=""
print(a,type(a))
b=bool(a)
print(b,type(b))#False
