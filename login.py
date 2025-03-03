def login(user, password):
    if user == "admin" and password == "pass123":
        print("Login successful")
    else:
        print("Invalid credentials")

username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)
