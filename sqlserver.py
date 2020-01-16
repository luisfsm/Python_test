def conexao(banco):
    import sqlite3
    conn = sqlite3.connect(banco)
    return conn


c = conexao('Banco_db.db')
c.cursor()
#c.execute('''CREATE TABLE PRODUTOS (PRODUTOS TEXT)''')

import pyodbc

server = "jupiter\\bv3"
database = 'Hering'
username = ''
password = ''
cnxn = pyodbc.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
save_arquivo = "produtos.txt"
for row in cursor.execute('''select rtrim(ltrim(produto)) from produtos'''):
#    c.execute('''insert into produtos values('+row+')''')
    print(str(row).replace('(','').replace(', )',''))

c.commit();
c.close()
#import pyodbc

#server = "jupiter\\bv3"
#database = 'Hering'
#username = 'sa'
#password = '312B1c3d34A@'
#cnxn = pyodbc.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()
#save_arquivo = "produtos.txt"
#for row in cursor.execute('select produto from produtos'):
#    with open(save_arquivo, 'w') as f:
 #       f.write(str(row))
