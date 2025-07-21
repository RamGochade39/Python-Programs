age=23
nums=[3,53,23,53,23,56]
b=bytes(age)
b1=bytes(nums)
print(b1)

for num in b1:
    print(num)

print(b1[0])
print("===================================================================")


bytearr=bytearray(nums)

print(bytearr)

for num in bytearr:
    print(num)

bytearr[0]=123
print("=========")
print(bytearr[0])