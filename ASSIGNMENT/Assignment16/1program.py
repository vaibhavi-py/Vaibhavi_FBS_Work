# 1) 

# PARAMETERIZED : 


class Book :
    def __init__ (self,bid,bname,price,author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author 
    
    def getData(self):
        return f'BOOK ID : {self.bid}\nBOOK NAME : {self.bname}\nPRICE : {self.price}\nAUTHOR : {self.author}'
    


#b1 = Book(101,'Python',2500,'Guido van rosum')
#print(b1.getData())



#PARAMETERLESS : 


class Book : 
    def __init__ (self):
        self.bid = ''
        self.bname = 0
        self.price = None
        self.author = ''

    def showBook(self):
        return f'BOOK ID : {self.bid}\nBOOK NAME : {self.bname}\nPRICE : {self.price}\nAUTHOR : {self.author}'
    

b2 = Book()

b2.bid = 102
b2.bname = 'Python'
b2.price = 3500
b2.author = 'Guido van rossum'

#print(b2.showBook())

#DESTRUCTOR 

class Book : 
    def __init__(self,bid,bname,price):
        self.bid = bid
        self.bname = bname
        self.price = price
        print('Object Created ')

    def __del__(self):
        print('Object Destroyed !')
    
#b3 = Book(103,'AI Basics',1500)

#del b3

# STATIC VARIABLE COUNT PROGRAM

class Book: 
    count = 0

    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
    
    def __del__(self):
        Book.count -= 1


b1 = Book(1, "Python", 3500, "Guido")
b2 = Book(2, "AI", 4500, "John")

print('Total Object :', Book.count)

del b1

print('After Deleting one object : ', Book.count)




