class Employee:
    def __init__(self,name,age,design):
        self.name = name
        self.age = age
        self.design = design
    
    def login(self,time):
        print(f'{self.name} is Login on {time}')

    def logout(self,time):
        print(f'{self.name} is Logout on {time}')

    def work(self,hours):
        print(f'{self.name} is worked for {hours}')

    def getDetails(self):
        print(f'Employee name {self.name}')
        print(f'Employee age {self.age}')
        print(f'Employee Designation {self.design}')

e1 = Employee('Akash','22',"SDE")
e2 = Employee('Swetha','22','Accountant')

e1.getDetails()
e1.login('7.00')
e1.logout('8.00')
e2.getDetails()

#====================================================
# Online store Program

class Product:
    def __init__(self,p_name,price,stock):
        self.p_name = p_name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f'Product Name: {self.p_name}, Price: {self.price}, Stock: {self.stock}')
    
    def update_price(self,newPrice):
        self.price = newPrice
        print(f'Updating price to {newPrice}...')
        print(f'New Price: {newPrice}')
    
    def update_stock(self, newstock):
        self.stock = newstock
        print(f'Updating stock to {newstock}...')
        print(f'New Stock: {newstock}')

p_name = input()
price = float(input())
stock = int(input())
newprice = float(input())
newstock = int(input())

p1 = Product(p_name,price,stock)
p1.display_info()
p1.update_price(newprice)
p1.update_stock(newstock)