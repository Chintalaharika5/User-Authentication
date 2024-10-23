import hashlib
import secrets
import getpass

user_data = {}

def register_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    salt = secrets.token_hex(16)  # Generate a random salt
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    user_data[username] = {'salt': salt, 'hashed_password': hashed_password}
    print("Registration successful!")

def login_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username in user_data:
        stored_data = user_data[username]
        hashed_password = hashlib.sha256((password + stored_data['salt']).encode()).hexdigest()
        if hashed_password == stored_data['hashed_password']:
            print("Login successful!")
            access_secured_page()
            return
    print("Invalid username or password.")

def access_secured_page():
    print("Welcome to the secured page!")
    print("You Are Selected")

# Example usage
register_user()
login_user()
