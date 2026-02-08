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
    id =  input("ID: ").strip()
    if id not in ids:
        print("Invalid ID...")
        return
    idx = ids.index(id)
    names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)
    print("Member successfully removed: ")

def update_rank(names, ranks, ids):
    upid = input("ID which will be updated: ").strip()
    if upid not in ids:
        print("Enter a valid ID...")
        return
    idx = ids.index(upid)
    new_rank = input("Enter new rank: ").strip()
    ranks[idx] = new_rank

def  display_roster(names, ranks, divs, ids):
    
    print("!!!CREW ROSTER!!!")
    
    if len(names) == 0:
        print("No crew in database...")
        return
    
    for i in range(len(names)):
        print(ids[i], names[i], divs[i], ranks[i])

def search_crew(names, ranks, divs, ids):
    term = input ("Enter name to search for: ").strip()
    found = False

    for i in range(len(names)):
        if term.names in names[i].lower():
            print( ids[i], names[i], ranks[i], divs[i])
            found = True

    if not found:
        print("No matching crew found...")

def filter_by_division(names, divs):
    choice = input("Enter division |Command, Operations, Security, Medical, Trainee|: ").strip()
    found = False
    
    for i in range(len(names)):
        if divs[i] == choice:
            print names[i] 
            found = True

    if not found: 
        print("No matching divisions found...")

def calculate_payroll(ranks):
    pay_ranks = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Ensign"]
    pay_values = [1000, 800, 600, 400, 100]
    total = 0
    for rank in ranks:
        if rank in pay_ranks:
            idx = pay_ranks.index(rank)
            total = total + pay_values[idx]
        else:
            pass
    return total

def 






    
    







    


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

