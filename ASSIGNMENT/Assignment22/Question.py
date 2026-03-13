import pickle
import os

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(self.eid, self.ename, self.basic)


file = "emp.dat"


def add_record():
    f = open(file, "ab")
    eid = int(input("Enter ID: "))
    name = input("Enter Name: ")
    basic = float(input("Enter Basic Salary: "))
    e = Emp(eid, name, basic)
    pickle.dump(e, f)
    f.close()


def display():
    try:
        f = open(file, "rb")
        while True:
            e = pickle.load(f)
            e.display()
    except:
        f.close()


def search():
    try:
        f = open(file, "rb")
        sid = int(input("Enter ID to search: "))
        found = False
        while True:
            e = pickle.load(f)
            if e.eid == sid:
                e.display()
                found = True
                break
    except:
        f.close()
        if not found:
            print("Record not found")


def delete():
    sid = int(input("Enter ID to delete: "))
    f = open(file, "rb")
    temp = open("temp.dat", "wb")

    try:
        while True:
            e = pickle.load(f)
            if e.eid != sid:
                pickle.dump(e, temp)
    except:
        pass

    f.close()
    temp.close()
    os.remove(file)
    os.rename("temp.dat", file)


def edit():
    sid = int(input("Enter ID to edit: "))
    f = open(file, "rb")
    temp = open("temp.dat", "wb")

    try:
        while True:
            e = pickle.load(f)
            if e.eid == sid:
                e.ename = input("Enter new name: ")
                e.basic = float(input("Enter new salary: "))
            pickle.dump(e, temp)
    except:
        pass

    f.close()
    temp.close()
    os.remove(file)
    os.rename("temp.dat", file)


while True:
    print("""
1. Add Record
2. Search Record
3. Delete Record
4. Edit Record
5. Display All
6. Exit
""")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_record()
    elif ch == 2:
        search()
    elif ch == 3:
        delete()
    elif ch == 4:
        edit()
    elif ch == 5:
        display()
    elif ch == 6:
        break