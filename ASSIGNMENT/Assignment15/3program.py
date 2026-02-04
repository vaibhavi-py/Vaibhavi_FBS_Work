# Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

# CONSTRUCTOR (PARAMETERIZED)

class Shirt:
    def __init__ (self,s_id,sname,type):
        self.s = s_id
        self.snm = sname
        self.t = type

    def ShowBook(self):
        print('SHIRT ID :', self.s)
        print('SHIRT NAME :', self.snm)
        print('TYPE :', self.t)

#s1 = Shirt(101,'COTTAN CANDY','Formal')
#s1.ShowBook()


#CONSTRUCTOR (PARAMERTERLESS)

class Shirt:
    def __init__ (self):
        self.s = None
        self.snm = None
        self.t = None

    def ShowBook(self):
        print('SHIRT ID :', self.s)
        print('SHIRT NAME :', self.snm)
        print('TYPE :', self.t)

#s2 = Shirt()
#s2.s = 101
#s2.snm = 'Cotton candy'
#s2.t = 'Formal'

#s2.ShowBook()


# DESTRUCTOR 

class Shirt:
    def __init__(self,s_id,sname,type):
        self.s_id = s_id
        self.snm = sname
        self.t = type

    def ShowBook(self):
        print('SHIRT ID :', self.s_id)
        
#DESTRUCTOR 
    def __del__ (self):
        print('CALLED DESTRUCTOR')
    

s3 = Shirt(101,'Cottan Candy','Formal')
s3.ShowBook()

del s3
