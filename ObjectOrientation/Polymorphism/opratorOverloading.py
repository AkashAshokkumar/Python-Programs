class Demo1:
    def disp1(self):
        print('Inside disp1')
    def __str__(self):
        return 'Hello'
class Demo2:
    def disp2(self):
        print("Inside disp2")
    def __str__(self):
        return 'Hi'
d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2)

'''
In Python if we print reference variable then internally python
will invoke __str__() which always returns string representation of an 
address of an object. 

In the above examples we have overridden __str__ methods in their
respective classes.
'''