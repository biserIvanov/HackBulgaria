import sql_manager
import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            while True:
                password = getpass.getpass('Enter your password: ')
                if len(password) > 8 and not username in password and any(char.isdigit() for char in password) \
                    and any(x.isupper() for x in password) and any(x.islower() for x in password) \
                    and any(c in password for c in '*$&'):
                    break                                                                           #test
                else:
                    print("pass must\n-be more than 8 characters\n -must have capital letters and numbers and a special symbol\n -not containing the username")

            sql_manager.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass('Enter your password: ')


            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")
        elif "send-reset-password" in command:
            sql_manager.send_resetPass(command[20:])
        elif "Reset-password" in command:
            sql_manager.reset_pass(command[15:])
        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("send-reset-password <username>")
            print("Reset-password <username>")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'balance':
            sql_manager.balance(logged_user.get_username())

        elif command == 'Deposit':
            sql_manager.deposit(logged_user.get_username())

        elif command == 'Withdraw':
            sql_manager.withdraw(logged_user.get_username())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
