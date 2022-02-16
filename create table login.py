import sqlite3
conn = sqlite3.connect('cloths.db')
conn.execute('''CREATE TABLE LOGIN(Username VARCHAR(255),
                                   Password VARCHAR(255))''')
conn.commit()
conn.close
