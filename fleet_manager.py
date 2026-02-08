def init_database():
    names = ["Picard", "Riker""", "Data", "Worf", "Leslie"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    divs = ["Command", "Command", "Operations", "Security"]
    ids= ["NCC-1701-A", "NCC-1701-B", "NCC-1701-C", "NCC-1701-D", "NCC-1701-E"]
    return names, ranks, divs, ids

def display_menu(current_user):
    print("\n--- FLEET MANAGEMENT SYSTEM ---")
    print("Logged in as:", current_user)
    print("1. Display roster")
    print("2. Add member")
    print("3. Remove member")
    print("4. Update rank")
    print("5. Search crew")
    print("6. Filter by division")
    print("7. Count officers")
    print("8. Calculate payroll")
    print("0. Exit")
    choice = input("Select option: ").strip()
    return choice
    
def add_members(names, ranks, divs, ids):
    


def main():
    names, ranks, divs, ids = init_database()
    print(names)
    print(ranks)
    print(divs)
    print(ids)

    if choice == 1:
        display_roster(names, ranks, divs, ids)
    
    user_name = input("Enter your full name: ").strip()
    choice = display_menu(user_name)

