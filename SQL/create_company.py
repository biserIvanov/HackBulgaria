import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
                      Employee(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)''')

cursor.execute('''INSERT INTO Employee(name, monthly_salary, yearly_bonus, position)
                  VALUES("IVAN Ivanov", 5000, 10000, "Software Developer")''')
cursor.execute('''INSERT INTO Employee(name, monthly_salary, yearly_bonus, position)
                  VALUES("Rado Rado", 500, 0, "Technical Support Intern")''')
cursor.execute('''INSERT INTO Employee(name, monthly_salary, yearly_bonus, position)
                  VALUES("Ivo Ivo", 10000, 100000, "CEO")''')
cursor.execute('''INSERT INTO Employee(name, monthly_salary, yearly_bonus, position)
                  VALUES("Petar Petrov", 3000, 1000, "Marketing Manager")''')
cursor.execute('''INSERT INTO Employee(name, monthly_salary, yearly_bonus, position)
                  VALUES("Maria Georgieva", 8000, 10000, "COO")''')

conn.commit()
conn.close()
