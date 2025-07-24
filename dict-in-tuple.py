tpl=(23,34,{"name":"ram","age":21,"graduation":2025},765)
print(tpl)

print(tpl[-2])

tpl[-2]["country"]="india"
print(tpl)

tpl[-2].popitem()
print(tpl)

