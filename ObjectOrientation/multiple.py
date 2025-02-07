class demo:
    def disp(self):
        print('Inside disp1 method')

class demo1:
    def disp(self):
        print('Inside disp2 method')

class demo2(demo, demo1):
    pass

d = demo2()
d.disp()