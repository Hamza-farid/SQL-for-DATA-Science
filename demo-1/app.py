from db_helper import DBhelper

class Flipkart:
    def __init__(self):
        # connect to db
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
1. Enter 1 to register
2. Enter 2 to login
3. Enter 3 to exit
""")    
        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        elif user_input == '3':
            print("Exiting...")
            exit()
        else:
            print("Invalid input, try again.")
            self.menu()

    def register(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        grade = input("Enter your grade: ")
        result = self.db.register_user(name, password,grade)
        if result:
            print("Registration successful!")
        else:
            print("Registration failed. Try again.")
    
    def login_menu(self):
        input("""
1. Enter 1 to see profile
2. Enter 2 to edit profile
3. Enter 3 to delete profile
4. Enter 4 to logout

""")
    
    def login(self):
        name =  input("Enter your name: ")
        password = input("Enter your password: ")
        result = self.db.search_user(name, password)
        if result:
            print(f"Login successful! Welcome {result[1]}, your grade is {result[3]}\nfull resord: {result}")
        else:
            print("Login failed. Invalid credentials.")
        self.menu()

obj = Flipkart()    