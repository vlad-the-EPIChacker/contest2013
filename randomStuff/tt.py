a = [{'a':10,'k':'a'}, {'a':23,'k':'l'},{'a':-2,'k':'l'}]
a.sort(key=lambda x: x['a'])
print(a)

