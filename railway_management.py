# railway_reservation_basic.py

# --- Data Storage (In-memory, lost when program exits) ---
# We'll use lists of dictionaries to store our data.

trains = [
    {"number": "TRN001", "name": "Guntur Express", "source": "Guntur", "destination": "Hyderabad", "total_seats": 50, "available_seats": 50, "fare": 350},
    {"number": "TRN002", "name": "Chennai Mail", "source": "Guntur", "destination": "Chennai", "total_seats": 60, "available_seats": 60, "fare": 400},
    {"number": "TRN003", "name": "Bangalore Pas", "source": "Guntur", "destination": "Bangalore", "total_seats": 40, "available_seats": 40, "fare": 500},
]

users = {
    "admin": "admin123", # Simple admin username and password
    "user1": "pass123"   # Simple user username and password
}

tickets = [] # Stores booked tickets

current_user = None # To keep track of logged-in user

# --- Helper Function (Simple PNR Generation) ---
def generate_pnr():
    import random
    import string
    # Generates a random 6-character alphanumeric PNR
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# --- User Functions ---

def register_user():
    print("\n--- User Registration ---")
    while True:
        username = input("Enter new username: ")
        if username in users:
            print("Username already exists. Please choose a different one.")
        else:
            password = input("Enter password: ")
            users[username] = password
            print(f"User '{username}' registered successfully!")
            break

def login_user():
    global current_user
    print("\n--- User Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        current_user = username
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password.")
        return False

def logout_user():
    global current_user
    current_user = None
    print("Logged out successfully.")

# --- Train Management Functions (Admin Only) ---

def add_train():
    if current_user != "admin":
        print("Access denied. Only admin can add trains.")
        return

    print("\n--- Add New Train ---")
    number = input("Enter Train Number (e.g., TRN004): ")
    for train in trains:
        if train["number"] == number:
            print("Train with this number already exists.")
            return

    name = input("Enter Train Name: ")
    source = input("Enter Source Station: ")
    destination = input("Enter Destination Station: ")
    total_seats = int(input("Enter Total Seats: ")) # Basic type conversion, no error handling
    fare = float(input("Enter Fare per seat: ")) # Basic type conversion

    new_train = {
        "number": number,
        "name": name,
        "source": source,
        "destination": destination,
        "total_seats": total_seats,
        "available_seats": total_seats, # Initially all seats are available
        "fare": fare
    }
    trains.append(new_train)
    print(f"Train '{name}' ({number}) added successfully.")

def view_all_trains():
    print("\n--- Available Trains ---")
    if not trains:
        print("No trains available.")
        return

    print(f"{'Number':<10} {'Name':<20} {'Source':<15} {'Destination':<15} {'Seats':<7} {'Fare':<8}")
    print("-" * 75)
    for train in trains:
        print(f"{train['number']:<10} {train['name']:<20} {train['source']:<15} {train['destination']:<15} {train['available_seats']:<7} {train['fare']:<8.2f}")

# --- Ticket Booking & Cancellation Functions ---

def search_and_book_ticket():
    if not current_user or current_user == "admin":
        print("Please log in as a regular user to book tickets.")
        return

    print("\n--- Search & Book Ticket ---")
    source = input("Enter Source Station: ")
    destination = input("Enter Destination Station: ")

    found_trains = []
    print("\nMatching Trains:")
    print(f"{'Number':<10} {'Name':<20} {'Source':<15} {'Destination':<15} {'Seats':<7} {'Fare':<8}")
    print("-" * 75)
    for train in trains:
        if train["source"].lower() == source.lower() and train["destination"].lower() == destination.lower():
            if train["available_seats"] > 0:
                print(f"{train['number']:<10} {train['name']:<20} {train['source']:<15} {train['destination']:<15} {train['available_seats']:<7} {train['fare']:<8.2f}")
                found_trains.append(train)
            else:
                print(f"{train['number']:<10} {train['name']:<20} {train['source']:<15} {train['destination']:<15} {'Full':<7} {train['fare']:<8.2f} (No seats available)")

    if not found_trains:
        print("No trains found for your route with available seats.")
        return

    selected_train_number = input("\nEnter Train Number to book (or 'q' to go back): ").upper()
    if selected_train_number == 'Q':
        return

    selected_train = None
    for train in found_trains:
        if train["number"] == selected_train_number:
            selected_train = train
            break

    if selected_train is None:
        print("Invalid train number selected.")
        return
    elif selected_train["available_seats"] == 0:
        print("Sorry, this train is full.")
        return

    # Basic Passenger Details
    passenger_name = input("Enter Passenger Name: ")
    passenger_age = int(input("Enter Passenger Age: "))
    passenger_gender = input("Enter Passenger Gender (M/F/Other): ")

    pnr = generate_pnr()
    seat_number = f"S{selected_train['total_seats'] - selected_train['available_seats'] + 1}" # Simple seat allocation

    new_ticket = {
        "pnr": pnr,
        "train_number": selected_train["number"],
        "train_name": selected_train["name"],
        "source": selected_train["source"],
        "destination": selected_train["destination"],
        "passenger_name": passenger_name,
        "age": passenger_age,
        "gender": passenger_gender,
        "seat_number": seat_number,
        "status": "CONFIRMED",
        "booked_by": current_user,
        "fare_paid": selected_train["fare"]
    }
    tickets.append(new_ticket)
    selected_train["available_seats"] -= 1

    print("\n--- Ticket Booked Successfully! ---")
    print(f"PNR: {pnr}")
    print(f"Train: {selected_train['name']} ({selected_train['number']})")
    print(f"Route: {selected_train['source']} to {selected_train['destination']}")
    print(f"Passenger: {passenger_name} ({passenger_age}, {passenger_gender})")
    print(f"Seat Number: {seat_number}")
    print(f"Fare Paid: Rs. {selected_train['fare']:.2f}")

def view_my_booked_tickets():
    if not current_user or current_user == "admin":
        print("Please log in as a regular user to view your tickets.")
        return

    print(f"\n--- Tickets Booked by {current_user} ---")
    user_tickets = [ticket for ticket in tickets if ticket["booked_by"] == current_user]

    if not user_tickets:
        print("You have no booked tickets.")
        return

    print(f"{'PNR':<8} {'Train':<10} {'Name':<20} {'Seat':<6} {'Status':<10} {'Fare':<8}")
    print("-" * 70)
    for ticket in user_tickets:
        print(f"{ticket['pnr']:<8} {ticket['train_number']:<10} {ticket['passenger_name']:<20} {ticket['seat_number']:<6} {ticket['status']:<10} {ticket['fare_paid']:<8.2f}")

def cancel_ticket():
    if not current_user or current_user == "admin":
        print("Please log in as a regular user to cancel tickets.")
        return

    print("\n--- Cancel Ticket ---")
    pnr_to_cancel = input("Enter PNR of the ticket to cancel: ").upper()

    found_ticket = None
    for ticket in tickets:
        # Check if the ticket exists, belongs to the current user, and is confirmed
        if ticket["pnr"] == pnr_to_cancel and ticket["booked_by"] == current_user and ticket["status"] == "CONFIRMED":
            found_ticket = ticket
            break

    if found_ticket:
        # Find the train to update available seats
        for train in trains:
            if train["number"] == found_ticket["train_number"]:
                train["available_seats"] += 1
                break
        
        found_ticket["status"] = "CANCELLED"
        print(f"Ticket with PNR {pnr_to_cancel} cancelled successfully.")
        print(f"Refund amount: Rs. {found_ticket['fare_paid'] * 0.90:.2f} (10% cancellation fee)") # Basic refund
    else:
        print("Ticket not found, or you do not have permission to cancel this ticket, or it's already cancelled.")

# --- Main Menus ---

def user_menu():
    while True:
        print(f"\n--- Welcome, {current_user}! ---")
        print("1. Book Ticket")
        print("2. View My Booked Tickets")
        print("3. Cancel Ticket")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            search_and_book_ticket()
        elif choice == '2':
            view_my_booked_tickets()
        elif choice == '3':
            cancel_ticket()
        elif choice == '4':
            logout_user()
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Add New Train")
        print("2. View All Trains")
        print("3. View All Booked Tickets (for admin reference)")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_train()
        elif choice == '2':
            view_all_trains()
        elif choice == '3':
            # Admin can view all tickets
            print("\n--- All Booked Tickets ---")
            if not tickets:
                print("No tickets booked yet.")
                return
            print(f"{'PNR':<8} {'Train':<10} {'P. Name':<15} {'Booked By':<10} {'Status':<10}")
            print("-" * 60)
            for ticket in tickets:
                print(f"{ticket['pnr']:<8} {ticket['train_number']:<10} {ticket['passenger_name']:<15} {ticket['booked_by']:<10} {ticket['status']:<10}")

        elif choice == '4':
            logout_user()
            break
        else:
            print("Invalid choice. Please try again.")

# --- Main Program Flow ---

def main():
    while True:
        print("\n--- Railway Ticket Reservation System ---")
        print("1. User Login")
        print("2. User Registration")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            if login_user():
                user_menu()
        elif choice == '2':
            register_user()
        elif choice == '3':
            # Simple admin login check
            username = input("Enter Admin Username: ")
            password = input("Enter Admin Password: ")
            if username == "admin" and password == "admin123":
                global current_user
                current_user = "admin" # Set current_user to admin
                print("Admin login successful!")
                admin_menu()
            else:
                print("Invalid admin credentials.")
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()