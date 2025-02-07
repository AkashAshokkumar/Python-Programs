set = {10,20,"Kodnest",True}
print(set, type(set)) # {True, 10, 20, 'Kodnest'} <class 'set'>

set.add(500)
print(set) #{True, 10, 20, 500, 'Kodnest'}

set.remove(20)
print(set) # {True, 'Kodnest', 10, 500}

poped_ele = set.pop()
print(poped_ele) # True
print(set) # {'Kodnest', 10, 500} Deletes any random element and return the element in the set