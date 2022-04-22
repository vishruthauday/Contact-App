def create_table(db):
    cur=db.cursor()
    cur.execute('create table if not exists  '+'contacts(Name text,Number text)')
    print('table created')
    db.commit()

def insert(db,name,num):
    cur=db.cursor()
    cur.execute('select * from contacts where Name=? or Number=?',(name,num))
    dt = cur.fetchall()
    if not dt:
        cur.execute('insert into contacts values(?,?)', (name,num))
        print('Contact Inserted.')
    else:
        print('Contact Already Exists.')
    db.commit()

def update(db,name,num):
    cur=db.cursor()
    cur.execute('select * from contacts where Name=?',(name,))
    chk=cur.fetchone()
    if chk is None:
        print('No Contact with that name present')
    else:
        cur.execute('update contacts set Number=? where Name=?',(num,name))
        print("Contact Updated")
    db.commit()

def view(db):
    cur=db.cursor()
    cur.execute('select * from contacts')
    a=cur.fetchall()
    if not a:
        print("No Contacts present.")
    else:
        print("Displaying Contacts:")
        for i in a:
            print(i)

def userview(db,ip):
    cur=db.cursor()
    cur.execute('select * from contacts where Name like "%{}%"'.format(ip))
    chk=cur.fetchall()
    if not chk:
        print("No contacts present")
    else:
        for i in chk:
            print(i)

def delete(db,name):
    cur=db.cursor()
    cur.execute('select * from contacts where Name=?',(name,))
    chk=cur.fetchone()
    if not chk:
            print("contact with name {} not found".format(name))
    else:
        cur.execute('delete from contacts where Name=?',(name,))
        print("contact with name {} deleted".format(name))
    db.commit()