def conexao(banco):
    import sqlite3
    conn = sqlite3.connect(banco)
    return conn


c = conexao('Banco_db.db')
c.cursor()


for t in c.execute("select * from stocks"):
    print(str(t))

import sqlite3


conn = sqlite3.connect('Banco_db.db')

c = conn.cursor()

#c.execute('''CREATE TABLE STOCKS (DATE TEXT, TRANS TEXT, SYMBOL TEXT, QTY REAL, PRICE REAL)''')

##c.execute("INSERT INTO STOCKS VALUES ('2020-01-05','BUY','RHAT',100,35.14)")

conn.commit()

for row in c.execute('select produto from produtos'):
    print(str(row).replace('(','').replace(')',''))

conn.close()




