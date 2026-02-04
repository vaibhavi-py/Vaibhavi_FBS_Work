## Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook

#CONSTRUCTOR (PARAMERTERIZED):
class Product:
    def __init__ (self,p_id,pname,price,quantity):
        self.p_id = p_id
        self.pnm = pname
        self.price = price
        self.quantity = quantity
    
    def ShowBook(self):
        print('PRODUCT ID :', self.p_id)
        print('PRODUCT NAME :', self.pnm)
        print('PRICE :', self.price)
        print('QUANTITY :', self.quantity)

m1 = Product(101,'Nike',2500,1)
m1.ShowBook()

#CONSTRUCTOR (PARAMETERLESS):

class Product:
    def __init__(self):
        self.p_id = None
        self.pnm = None
        self.price = None
        self.quantity = None
    
    def ShowBook (self):
        print('PRODUCT ID :', self.p_id)
        print('PRODUCT NAME :', self.pnm)
        print('PRICE :', self.price)
        print('QUANTITY :', self.quantity)

m2 = Product()
m2.p_id = 101
m2.pnm = 'Nike'
m2.price = 2500
m2.quantity = 1

m2.ShowBook() 

# DESTURCTOR 

class Product:

    def __init__ (self,p_id,pname,price,quantity):
        self.p_id = p_id
        self.pnm = pname
        self.price = price
        self.quantity = quantity
    
    def ShowBook(self):
        print('PRODUCT ID :', self.p_id)
        print('PRODUCT NAME :', self.pnm)
    
    #DESTRUCTOR 
    def __del__(self):
        print('Called Destructor')
    
m3 = Product(103,'Sprax',3500,2)
m3.ShowBook()
del m3 