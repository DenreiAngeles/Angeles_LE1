# Dictionary to store game library with their quantities and rental costs
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    # Add more games as needed
}

# Dictionary to store user accounts with their balances and points
user_accounts = {}

# Admin account details
admin_username = "admin"
admin_password = "adminpass"

def separator():
    print("-"*100)

# Function to display available games with their numbers and rental costs
def display_available_games():
    separator()
    print("Available Games:")
    for index, (games, details) in enumerate(game_library.items(), start = 1):
        copies = details["quantity"]
        cost = details["cost"]
    print(f"{index}. {games}\n\t>>copies: {copies}\n\t>>cost: {cost}")

# Function to register a new user
def register_user():
    separator()
    print("Register:")
    username = input("Enter New Username: ")
    if username == "":
        return
    if username in user_accounts:
        print("Username already taken. Please use another username.")
        input("Press Enter to continue...")
        return
    password = input("Enter New Password: ")
    if password == "":
        return
    user_accounts[username] = {"username": username, "password": password, "balance": 1.0, "points": 0, "excess_pts": 0, "inventory": []}
    print("Account Successfully Created! Proceed to Login.")
    input("Press Enter to continue...")

def log_in_user():
    separator()
    print("Log In:")
    username = input("Enter your username: ")
    if username == "":
        return
    if username not in user_accounts:
        print("Username not found. Please Register.")
        input("Press Enter to continue...")
        return
    while True:
        password = input("Enter your password: ")
        if password == "":
            return
        if password != user_accounts[username]["password"]:
            print("Incorrect Password")
            input("Press Enter to continue...")
            continue
        return username

# Function to rent a game
def rent_game(username):
    pass

# Function to return a game
def return_game(username):
    pass

# Function to top-up user account
def top_up_account(username, amount):
    pass

# Function to display user's inventory
def display_inventory(username):
    pass

# Function for admin to update game details
def admin_update_game(username):
    pass

# Function for admin login
def admin_login():
    pass

# Admin menu
def admin_menu():
    pass

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    pass

# Function to display game inventory
def display_game_inventory():
    pass

# Function to handle user's logged-in menu
def logged_in_menu(username):
    pass

# Function to check user credentials
def check_credentials(username, password):
    pass
    
# Main function to run the program
def main():
    pass

if __name__ == "__main__":
    main()