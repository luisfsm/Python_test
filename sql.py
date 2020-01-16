import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-IKAKRES;'
                      'Database=crm;'
                      'Trusted_Connection=yes;'
                      )
cursor = conn.cursor()
cursor.execute('SELECT xml FROM xml_nfe')

save_path_file = "Nfe.xml"

for row in cursor:
    with open(save_path_file, "w") as f:
        f.write(str(row).replace("('", "").replace("', )", ""))
print(save_path_file)