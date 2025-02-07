# Print First runner up in the List.
'''li = list(map(int, input().split(",")))
li = list(set(li))
li.sort() # Sort Method won't Return Anything. It should be in with out an asignment
print(li[1]) '''

#Packing and Unpacking Concept --->

'''name,*mark, age = ["Pooja", 10,20,30,22]
print("Name is:",name , "Marks are:",mark, "Age is:",age)'''

li = [10,20,30,40]
for idx,ele in enumerate(li):
    print(idx,ele)

#Write a python Program to print all even index element

li1 = [1,2,3,4,5,6]
for idx,ele in enumerate(li1):
    if (ele % 2 == 0) :
        print(idx,ele)

# Subset will check all the element are present in the given list.
s1 = {1,2,3}
s2 = {1,2,3,4,5}
print(s1.issubset(s2)) #All ele of s1 are present in s2?True
print(s2.issubset(s1)) #All ele of s2 are present in s1?False