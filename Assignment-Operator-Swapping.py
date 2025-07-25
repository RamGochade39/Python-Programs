#Swapping Of Two Numbers Using Different Techniques

a=10
b=20;
#1
a,b=b,a
print("a -> ",a," b-> ",b)


a=100
b=200
#2
c=a
a=b
b=c
print("a -> ",a," b-> ",b)


a=1
b=2
#3
a=a+b
b=a-b
a=a-b
print("a -> ",a," b-> ",b)

a=100
b=200
#4
a=a*b
b=a//b
a=a//b
print("a -> ",a," b-> ",b)
