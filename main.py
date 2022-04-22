import sqlite3
import contact

db=sqlite3.connect("contacts.db")
contact.create_table(db)
print("Select one:")
while True:
    print("1.Add contact\n2.Update Contact\n3.Delete Contact\n4.print\n5.userview\n6.exit\n")
    i=int(input("Enter Your Choice:"))
    if i==1:
        name=input("Enter Name:")
        num=int(input("Enter Number:"))
        contact.insert(db,name,num)
    elif i==2:
        name=input("Enter Name:")
        num=int(input("Enter Number:"))
        contact.update(db, name, num)
    elif i==3:
        name=input("Enter Name:")
        contact.delete(db, name)
    elif i==4:
        contact.view(db)
    elif i==5:
        ip=input("Enter value:")
        contact.userview(db, ip)
    elif i==6:
        exit()


db.close()