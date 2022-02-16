import sqlite3
conn = sqlite3.connect('cloths.db')
conn.execute('''CREATE TABLE REGISTRATION(Full_name VARCHAR(255),
                                   Plot_no VARCHAR(255),
                                   Street VARCHAR(255),
                                   State VARCHAR(255),
                                   City VARCHAR(255),
                                   Pincode VARCHAR(255),
                                   Email VARCHAR(255),
                                   Password VARCHAR(255),
                                   Mobile_no VARCHAR(255))''')
conn.commit()
conn.close
