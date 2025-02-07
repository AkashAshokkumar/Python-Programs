li1 = [1,2,3,4,5]

dup_li = [i for i in li1]
print(dup_li)

even_li = [i for i in li1 if i%2 == 0]
print(even_li)

an_li = [i**i for i in li1]
print(an_li)

even_odd = ['even' if i%2==0 else 'odd' for i in li1]
print(even_odd)