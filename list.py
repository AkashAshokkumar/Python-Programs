li1 = [10,20,1.5,True,"Akash"]
li1.append(50) # adds a element in the list
print(li1)

li1.insert(1, 12) # Inserts the Given Element
print(li1)

li1.remove(12) # Removes the Given element
print(li1)

print(125 in li1)
print(125 not in li1)

li1.pop() #Deletes last element in the list and return in the element
print(li1)

rem_ele = li1.pop(2)
print(rem_ele)
print(li1)

del li1[1] # IT will delete from the list and not return like pop
print(li1)
