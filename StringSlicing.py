str="PYTHON";

print(len(str))
print(str)

print("=====================================================")
#str[startInd:endInd]
print(str[0:6])
print(str[1:6])
print(str[2:5])
print(str[3:6])
print(str[5:6])
print("=====================================================")
#minus indexing
print(str[1:-1])
print(str[2:-2])
print(str[1:-1])
print(str[-122:-1])
print(str[-122:0])#space
print(str[0:123])#will print till the length then nothing
print(str[-2:-4])

print("=====================================================")
#start index only
print(str[1:])
print(str[-5:])
print(str[-2:])
print(str[2:])
print(str[-6:])
print(str[-1:])

print("=====================================================")
#end index only
print(str[:123])
print(str[:-1])
print(str[:1])
print(str[:4])
print(str[:-5])
print(str[:-4])

