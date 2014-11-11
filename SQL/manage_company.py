import sqlite3


conn = sqlite3.connect('company.db')
cursor = conn.cursor()


def list_employees():
    result = cursor.execute("SELECT * FROM Employee")
    for row in result:
        print(row)


def monthly_spending():
    result = cursor.execute("SELECT SUM(monthly_salary) FROM Employee")
    result = result.fetchone()
    return result[0]


def yearly_spending():
    result = monthly_spending() * 12
    return result


def add_employee():
    name = input("Enter name: ")
    monthly_salary = input("Enter monthly_salary: ")
    yearly_bonus = input("Enter yearly_bonus: ")
    position = input("Enter position: ")

    cursor.execute('''INSERT INTO Employee(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
    conn.commit()
    print("Done")


def delete_employee(employee_id):
    cursor.execute('''DELETE FROM Employee WHERE id = ?''', (employee_id,))
    conn.commit()
    print("Done")


def update_employee(employee_id):
    name = input("Enter name: ")
    monthly_salary = input("Enter monthly_salary: ")
    yearly_bonus = input("Enter yearly_bonus: ")
    position = input("Enter position: ")

    cursor.execute('''UPDATE Employee SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?''',
                   (name, monthly_salary, yearly_bonus, position, employee_id))
    conn.commit()
    print("Done")


choice = "0"
while choice != "Exit" or choice != "exit":
    choice = input(
        "========================================\nChooce an option:  \n\n - list_employees\n - monthly_spending\n - yearly_spending\n - add_employee\n - delete_employee <employee_id>\n - update_employee <employee_id>\n - Exit \n")
    if choice == "list_employees":
        list_employees()
    elif choice == "monthly_spending":
        result = monthly_spending()
        print("The company is spending $" + str(result) + " every month!")
    elif choice == "yearly_spending":
        result = yearly_spending()
        print("The company is spending $" + str(result) + " every year!")
    elif choice == "add_employee":
        add_employee()
    elif "delete_employee" in choice:
        delete_employee(int(choice[16:]))
    elif "update_employee" in choice:
        update_employee(int(choice[16:]))
