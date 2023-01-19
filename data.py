import sqlite3
#this is how you will edit data
'''multiline comment finally'''
connection=sqlite3.connect('database.db')

cur = connection.cursor()

cur.execute("INSERT INTO suser(sname, gr_no, branch, email, passw) VALUES (?, ?, ?, ?, ?)",
                    ('raviraj', '11', 'extc', 'email1@co.in', 'pass')
                    )

cur.execute("INSERT INTO suser(sname, gr_no, branch, email, passw) VALUES (?, ?, ?, ?, ?)",
                    ('sham', '12', 'extc', 'email2@co.in', 'pass')
                    )

cur.execute("INSERT INTO suser(sname, gr_no, branch, email, passw) VALUES (?, ?, ?, ?, ?)",
                    ('naina', '13', 'extc', 'email3@co.in', 'pass')
                    )   

cur.execute("INSERT INTO posts(title, content, price, seller_ID) VALUES (?, ?, ?, ?)",
                    ('first item', 'about first item', '38', '1')
                    )

cur.execute("INSERT INTO posts(title, content, price, seller_ID) VALUES (?, ?, ?, ?)",
                    ('second item', 'about second item', '47', '3')
                    )

#dog damn that relation thingy doesn't work in here
                    
connection.commit()
connection.close()
