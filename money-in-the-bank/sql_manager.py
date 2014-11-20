import requests
import sqlite3
import hashlib
import smtplib
from Client import Client
from time import time
from random import randint

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    cursor.execute('''PRAGMA foreign_keys = ON;''')
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT)'''

    cursor.execute(create_query)
    create_query = '''create table if not exists
        clientsLogin(id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                failLogins INTEGER,
                timeOf DOUBLE,
                FOREIGN KEY (client_id) REFERENCES clients(id))'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    param = (new_message, logged_user.get_id())
    cursor.execute(update_sql, param)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    param = (new_pass, logged_user.get_id())
    cursor.execute(update_sql, param)
    conn.commit()


def register(username, password):
    m = hashlib.sha1()
    password = password.encode('utf-8')
    m.update(password)
    insert_sql = "INSERT INTO clients (username, password) VALUES (?, ?)"
    param = (username, m.digest())
    cursor.execute(insert_sql, param)
    conn.commit()


def balance(username):
    select_query = "SELECT balance FROM clients WHERE username = ?"
    param = (username,)
    cursor.execute(select_query, param)
    user_balance = cursor.fetchone()[0]
    print("Your balance is " + str(user_balance) + "$")


def deposit(username):
    amount = input("Enter amount: ")
    select_query = "SELECT balance FROM clients WHERE username = ?"
    param = (username,)
    cursor.execute(select_query, param)
    user_balance = cursor.fetchone()[0]
    user_balance += int(amount)
    update_query = '''UPDATE clients SET balance = ? WHERE username = ?'''
    param = (user_balance, username)
    cursor.execute(update_query, param)
    conn.commit()
    print("Done")


def withdraw(username):
    amount = int(input("Enter amount: "))
    select_query = "SELECT balance FROM clients WHERE username = ?"
    param = (username,)
    cursor.execute(select_query, param)
    user_balance = cursor.fetchone()[0]
    if amount < user_balance:
        user_balance -= amount
        update_query = '''UPDATE clients SET balance = ? WHERE username = ?'''
        param = (user_balance, username)
        cursor.execute(update_query, param)
        conn.commit()
        print("Done")
    else:
        print("not enough money in your account")


def add_failLogin(user_id):
    t = time()
    insert_query = "INSERT INTO clientsLogin(client_id, failLogins, timeOf) VALUES (?,1,?)"
    param = (user_id, t)
    cursor.execute(insert_query, param)
    conn.commit()


def update_failLogin(user_id):
    select_query = "SELECT failLogins FROM clientsLogin WHERE client_id = ? LIMIT 1"
    param = (user_id,)
    cursor.execute(select_query, param)
    fails = cursor.fetchone()[0] + 1
    update_query = '''UPDATE clientsLogin SET failLogins = ? WHERE client_id = ?'''
    param = (fails, user_id)
    cursor.execute(update_query, param)
    conn.commit()
    print("end")


def isBlocked(username):
    select_query = "SELECT id FROM clients WHERE username = ?"
    param = (username,)
    cursor.execute(select_query, param)
    user_id = cursor.fetchone()[0]
    select_query = "SELECT failLogins, timeOf FROM clientsLogin WHERE client_id = ?"
    param = (user_id,)
    cursor.execute(select_query, param)
    result = cursor.fetchone()
    if str(result) == "None":
        return False
    failsNum = result[0]
    failTime = result[1]
    print("failsNum = " + str(failsNum))
    t = time()
    if failTime - t > 0:
            print("you are blocked")
            return True
    if failsNum > 5:
        t = time()
        if t - failTime < 300:          #ako e feilnal 10 puti za 5 min
            unlockTime = t + 300
            update_query = '''UPDATE clientsLogin SET timeOf = ?, failLogins = 0 WHERE client_id = ?'''
            param = (unlockTime, user_id)
            cursor.execute(update_query, param)
            conn.commit()
            return True
    else:
        return False


def login(username, password):
    m = hashlib.sha1()
    password = password.encode('utf-8')
    m.update(password)
    if isBlocked(username):
        print("You are blocked for 5 minutes!")
        return False
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
    param = (username, m.digest())
    cursor.execute(select_query, param)
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        select_query = "SELECT id FROM clients WHERE username = ? LIMIT 1"
        param = (username,)
        cursor.execute(select_query, param)
        user1 = cursor.fetchone()[0]        #id of the user who failed to login

        select_query = "SELECT client_id FROM clientsLogin WHERE client_id = ? LIMIT 1"
        param = (user1,)
        cursor.execute(select_query, param)
        user = cursor.fetchone()
        user2 = str(user)
        #print(user2)
        if user2 == "None":
            add_failLogin(user1)
        else:
            update_failLogin(user1)
        return False

def send_resetPass(username):
    select_query = "SELECT email FROM clients WHERE username = ?"
    param = (username,)
    cursor.execute(select_query, param)
    user_email = cursor.fetchone()[0]

    randomInt = str(randint(1, 50000))
    randomInt = randomInt.encode('utf-8')
    new_pass = hashlib.sha1(randomInt).hexdigest()

    update_query = '''UPDATE clients SET password = ? WHERE username = ?'''
    param = (new_pass, username)
    cursor.execute(update_query, param)
    conn.commit()

    message = 'type Reset-password <username> to change password ;)' + '\n' + 'Here is your verification code: ' + str(new_pass)
    fromaddr = 'biserivanov08@gmail.com'

    username = 'biserivanov08@gmail.com'
    password = ''     #!!!

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, user_email, message)
    server.quit()
    print('done')


def reset_pass(username):
    theHashCode = input("Enter the hashcode sent to your email")
    select_query = "SELECT password FROM clients WHERE username = ?"
    param = (username,)
    cursor.execute(select_query, param)
    user_pass = cursor.fetchone()[0]
    if theHashCode == user_pass:
        new_pass = input("Enter the new password: ")
        m = hashlib.sha1()
        new_pass = new_pass.encode('utf-8')
        m.update(new_pass)
        new_pass = m.digest()

        update_query = '''UPDATE clients SET password = ? WHERE username = ?'''
        param = (new_pass, username)
        cursor.execute(update_query, param)
        conn.commit()
        print("password changed!")
    else:
        print("wrong code, try again")
