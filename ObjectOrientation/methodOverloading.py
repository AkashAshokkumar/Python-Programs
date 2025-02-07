class demo:
    def disp1(self):
        print('inside 1st method')

    def disp2(self,a):
        print('inside 1st method')

    def disp3(self,a,b):
        print('inside 1st method')

d = demo()
d.disp1()
#d.disp1(10)
#d.disp1(10,20) We cant method overload in Python Like Javascript and if you overload The last Method will be exicuted.