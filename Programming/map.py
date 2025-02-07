'''tup = ('10','20','30','40')
tup = tuple(map(int,tup))
print(tup)

tup1 = tuple(map(int, input('Enter Your Values').split()))
print(tup1) '''

li = list(map(int, input().split(",")))
li = set(li)
li = list(li).sort()
print(li[1])