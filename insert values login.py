import sqlite3
conn = sqlite3.connect('cloths.db')
conn.execute('''INSERT INTO LOGIN(Username,
                                   Password)VALUES("piyush@gmail.com","123456789")''')
conn.commit()
conn.close
