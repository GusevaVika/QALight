import sqlite3
conn = sqlite3.connect("SecretData.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Employees
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    'full name' TEXT,
                                    'age' INTEGER ,
                                    'address' TEXT)''')
cursor.execute('''CREATE TABLE Salary
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    id_Employee INTEGER,
                                    bonus INTEGER,
                                    net salary INTEGER,
                                    experience FLOAT,
                                    FOREIGN KEY (id_Employee) REFERENCES Employees(id))''')
cursor.execute('''CREATE TABLE Position
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    id_Employees INTEGER,
                                    department TEXT,
                                    position TEXT,
                                    skillsDevelopment TEXT,
                                    FOREIGN KEY (id_Employees) REFERENCES Employees(id))''')
conn.commit()
