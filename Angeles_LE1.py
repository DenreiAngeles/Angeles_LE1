# Dictionary to store game library with their quantities and rental costs
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2.25},
    "Super Mario Bros": {"quantity": 5, "cost": 3.40},
    "Tetris": {"quantity": 2, "cost": 1.50},
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
    balance = user_accounts[username]["balance"]
    print(f"\nCredits: {balance:.2f}\n")

def excess_points_system(username, game):
    decimal_excess = game_library[game]["cost"] - int(game_library[game]["cost"])
    excess = game_library[game]["cost"] - ((game_library[game]["cost"] // 2)*2)
    user_accounts[username]["excess_pts"] += (excess)
    if user_accounts[username]["excess_pts"] >= 2:
        user_accounts[username]["points"] += user_accounts[username]["excess_pts"] // 2
        user_accounts[username]["excess_pts"] -= 2

# Function to rent a game
def rent_game(username):
    while True:
        try:
            separator()
            display_available_games()
            display_balance(username)
            gameList = list(game_library.keys())
            game_index = input(f"Enter the number of the game you want to rent (from 1 to {len(gameList)}): ")
            if game_index == "":
                return
            game_index = int(game_index) - 1
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
            excess_points_system(username, game)
            user_accounts[username]["inventory"].append(game)
            print(f"Rental Successful. Your remaining credits: {user_accounts[username]["balance"]}")
            input("Press Enter to continue...")
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
        return
    for index, game in enumerate(stash(), start = 1):
        print(f"{index}. {game}")

# Function to return a game
def return_game(username):
    while True:
        try:
            separator()
            display_user_stash(username)
            stash = user_accounts[username]["inventory"]
            return_game = input(f"Enter the number of the game you want to return (from 1 to {len(stash)}): ")
            if return_game == "":
                return
            return_game = int(return_game) - 1
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

# Function to top-up user account
def top_up_account(username):
    while True:
        try:
            separator()
            display_balance(username)
            deposit = float(input("Enter the amount of credits you want to deposit: "))
            if deposit == "":
                return
            if deposit <= 0:
                print("You can only enter a positive amount.")
                input("Press Enter to continue...")
                continue
            user_accounts[username]["balance"] += deposit
            print("Deposit Successful.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            input("Press Enter to continue...")

# Function for admin to update game details
def admin_update_game(username):
    pass

# Function for admin login
def admin_login():
    separator()
    print("Admin Log In:")
    username = input("Enter Username: ")
    if username != admin_username:
        print("Incorrect username.")
        return
    password = input("Enter Password: ")
    if password != admin_password:
        print("Incorrect password.")
        return
    return True

# Admin menu
def admin_menu():
    pass

def display_points(username):
    print(f"Points: {user_accounts[username]["points"]}")

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    while True:
        try:
            separator()
            display_available_games()
            display_points(username)
            gameList = list(game_library.keys())
            print("Note: You can only redeem a free rental if you have atleast 3 points.")
            game_index = int(input(f"Enter the number of the game you want to redeem (from 1 to {len(gameList)}): ")) - 1
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
            if user_accounts[username]["points"] < 3:
                print("You don't have enough points. Please rent a game to gain points.")
                input("Press Enter to continue...")
                return
            game_library[game]["quantity"] -= 1
            user_accounts[username]["points"] -= 3
            user_accounts[username]["inventory"].append(game)
            print(f"Rental Successful. Your remaining points: {user_accounts[username]["points"]}")
            input("Press Enter to continue...")
        except ValueError:
            print("Invalid Input. Please enter a valid input.")
            input("Press Enter to continue...")
        break

# Function to handle user's logged-in menu
def logged_in_menu(username):
    while True:
        separator()
        print(f"Welcome Back, {username}!")
        print("What would you like to do today?")
        print(f"\nCredits: {user_accounts[username]["balance"]}\tPoints: {user_accounts[username]["points"]}\n")
        print("1. Top Up\n2. Rent Games\n3. Return Games\n4. Redeem Free Rental\n5. Log Out")
        choice = input("Enter the number of what you want to do: ")
        if choice == "1":
            top_up_account(username)
        elif choice == "2":
            rent_game(username)
        elif choice == "3":
            return_game(username)
        elif choice == "4":
            redeem_free_rental(username)
        elif choice == "5":
            break
        else:
            print("Invalid Input. Please enter a valid input.")
            input("Press Enter to continue...")
    
# Main function to run the program
def main():
    while True:
        separator()
        print("Rent-a-Game")
        print("\nWelcome to Rent-a-Game! What would you like to do today?")
        print("1. Display Available Games\n2. Register\n3. Log In\n4. Admin Log In\n5. Exit ")
        choice = input("Enter the number of what you want to do: ")
        if choice == "1":
            display_available_games()
            input("\nPress Enter to Continue...")
        elif choice == "2":
            register_user()
        elif choice == "3":
            login = log_in_user()
            if login:
                logged_in_menu(login)
        elif choice == "4":
            admin_login()
            if admin_login() == True:
                admin_menu()
        elif choice == "5":
            print("Thank you for your patronage!")
            break
        else:
            print("Invalid Input. Please enter a valid input.")
            input("Press Enter to Continue...")
            continue

if __name__ == "__main__":
    main()