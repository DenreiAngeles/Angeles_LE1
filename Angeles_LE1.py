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

def display_balance(username):
    credits = user_accounts[username]["balance"]
    print(f"\nCredits: {credits:.2f}\n")

# Function to rent a game
def rent_game(username):
    while True:
        try:
            separator()
            display_available_games()
            display_balance(username)
            gameList = list(game_library.keys())
            game_index = int(input(f"Enter the number of the game you want to rent (from 1 to {len(gameList)}): ")) - 1
            if game_index == "":
                return
            if game_index not in range(len(gameList)):
                print(f"Please enter only a number from 1 to {len(gameList)}.")
                input("Press Enter to continue...")
                continue
            game = gameList[game_index]
            if game_library[game]["quantity"] <= 0:
                print("There are no available copies left for this game.")
                input("Press Enter to continue...")
                continue
            if game_library[game]["cost"] > user_accounts[username]["balance"]:
                print("You don't have enough credits. Please top-up.")
                input("Press Enter to continue...")
                return
            game_library[game]["quantity"] -= 1
            user_accounts[username]["balance"] -= game_library[game]["cost"]
            user_accounts[username]["points"] += game_library[game]["cost"] // 2
            user_accounts[username]["excess_pts"] += game_library[game]["cost"] % 2
            if user_accounts[username]["excess_pts"] == 2:
                user_accounts[username]["points"] += 1
                user_accounts[username]["excess_pts"] -= 2
            user_accounts[username]["inventory"].append(game)
            print(f"Rental Successful. Your remaining credits: {user_accounts[username]["balance"]}")
            input("Press Enter to continue...")
        except ValueError:
            print("Invalid Input. Please enter a valid input.")
            input("Press Enter to continue...")
        break

# Function to return a game
def return_game(username):
    while True:
        try:
            separator()
            display_available_games()
            display_balance(username)
            gameList = list(game_library.keys())
            game_index = int(input(f"Enter the number of the game you want to rent (from 1 to {len(gameList)}): ")) - 1
            if game_index == "":
                return
            if game_index not in range(len(gameList)):
                print(f"Please enter only a number from 1 to {len(gameList)}.")
                input("Press Enter to continue...")
                continue
            game = gameList[game_index]
            if game_library[game]["quantity"] <= 0:
                print("There are no available copies left for this game.")
                input("Press Enter to continue...")
                continue
            if game_library[game]["cost"] > user_accounts[username]["balance"]:
                print("You don't have enough credits. Please top-up.")
                input("Press Enter to continue...")
                return
            game_library[game]["quantity"] -= 1
            user_accounts[username]["balance"] -= game_library[game]["cost"]
            user_accounts[username]["points"] += game_library[game]["cost"] // 2
            user_accounts[username]["excess_pts"] += game_library[game]["cost"] % 2
            if user_accounts[username]["excess_pts"] == 2:
                user_accounts[username]["points"] += 1
                user_accounts[username]["excess_pts"] -= 2
            user_accounts[username]["inventory"].append(game)
            print(f"Rental Successful. Your remaining credits: {user_accounts[username]["balance"]}")
            input("Press Enter to continue...")
        except ValueError:
            print("Invalid Input. Please enter a valid input.")
            input("Press Enter to continue...")
        break

# Function to top-up user account
def top_up_account(username, amount):
    while True:
        try:
            separator()
            display_user_stash(username)
            stash = user_accounts[username]["inventory"]
            return_game = int(input(f"Enter the number of the game you want to return (from 1 to {len(stash)}): ")) - 1
            if return_game == "":
                return
            if return_game not in range(len(stash)):
                print(f"Please enter only a number from 1 to {len(stash)}.")
                continue
            game = stash[rent_game]
            game_library[game]["quantity"] += 1
            stash.pop(return_game)
        except ValueError:
            print("Invalid Input. Please enter a valid input.")
            input("Press Enter to continue...")
        break

# Function to display user's inventory
def display_user_stash(username):
    print("Your Rented Games:")
    stash = user_accounts[username]["inventory"]
    if not stash:
        print("Your inventory is empty...")
    for index, game in enumerate(stash.items(), start = 1):
        print(f"{index}. {game}")

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