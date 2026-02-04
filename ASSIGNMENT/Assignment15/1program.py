## Create a class Book with members as bid,bname,price and author.Add following
#methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

# a)  CONSTRUCTOR   
# Parameterized (Constructor)
class Book :
    def __init__ (self,bid,bname,price,author): 
        self.b = bid
        self.n = bname
        self.p = price
        self.a = author


    def ShowBook (self):
        print('BOOK ID :', self.b)
        print('BOOK NAME :',self.n)
        print('PRICE : ',self.p)
        print('AUTHOR :', self.a)
    
b1 = Book(101,'Core Python',450,'Guido')
b1.ShowBook()



# parameterless (Constructor)

class Book :
    def __init__(self):
        self.bid = None
        self.n = None
        self.p = None 
        self.a = None
    
    def ShowBook (self):
        print('BOOK ID :',self.bid)
        print('BOOK NAME :', self.n)
        print('PRICE :', self.p)
        print('AUTHOR :', self.a)

b2 = Book()
b2.bid = 101
b2.n = 'Python'
b2.p = 450
b2.a = 'Guido'

b2.ShowBook()


# b) DESTRUCTOR .

class Book:

    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Constructor Called")

    def ShowBook(self):
        print("Book ID   :", self.bid)
        print("Book Name :", self.bname)

    # Destructor
    def __del__(self):
        print("Destructor Called, Object Deleted")


b3 = Book(103, "C++", 700, "Bjarne")
b3.ShowBook()

del b3     # Manually deleting object

