def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Leslie"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant","Ensign"]
    divs = ["Command", "Operations", "Security", "Medical", "Trainee"]
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
    new_name = input("Name: ").strip()
    new_rank = input("Rank: ").strip()
    new_div = input("Division: ").strip()
    new_id = input("ID: ").strip()
    if new_id in ids:
        print("Error: ID already exists!!")
        return
    elif new_rank not in ranks:
        print("Please choose a valid rank...")
        return
    elif new_div not in divs:
        print("Please enter a valid division...")
        return
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print("Crew member added successfully")
       
def remove_member(names, ranks, divs, ids):
    id =  input("ID ").strip()
    if id not in ids:
        print("Invalid ID...")
        return
    idx = ids.index(id)
    names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)
    print("Member successfully removed: ")





    


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

