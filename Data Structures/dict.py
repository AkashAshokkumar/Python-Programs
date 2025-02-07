d1 = {'name':'Akash', 'Age':'21', 'phone':'12345'}
print(d1, type(d1)) # {'name': 'Akash', 'Age': '21', 'phone': '12345'} <class 'dict'> It is Ordered sequence

d1['name'] = "Swetha"
print(d1) # {'name': 'Swetha', 'Age': '21', 'phone': '12345'} Dictionary are Mutable

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)
