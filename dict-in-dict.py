d1={"name":"ram","marks":{"en":54,'sc':57,'java':98},"class":"BCS-TY"}

print(d1)

print(d1.get("marks"))

d1.get("marks")["c"]=89
print(d1)

print(d1.get("marks")["en"])

d1["marks"].popitem()
print(d1)