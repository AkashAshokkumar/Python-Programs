class demo:
    def __init__(self):
        self.x = 100

    def __init__(self):
        self.x = 200

d = demo()
print(d.x)


# Method Chaining using super method

class grand:
    def cook(self):
        print('Grand parent can cook Briyani')

class parent(grand):
    def cook(self):
        print('parent can cook Noodles')

class child(parent):
    def cook(self):
        print('Child cant cook Briyani')
        super().cook()
        super(parent, self).cook()

d = child()
d.cook()
