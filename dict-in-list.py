lst=[34,{"en":54,'sc':57,'java':98},56,87,34,34]

for k in lst:
    print(k)

print(lst[1])

print(lst[1].get("java"))

lst[1]["c++"]=43
print(lst)

for k,v in lst[1].items():
    print(k,"====>",v)

lst[1]["c++"]=95
print(lst)