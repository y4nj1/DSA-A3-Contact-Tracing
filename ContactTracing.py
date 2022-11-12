# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# =================== CODE PROPER =========================
# [1] Display Menu
def menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(' '*4 + "Yanji's Contact Tracing Directory")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("=========================================")
    print(' '*6 + "||       MAIN MENU          ||")
    print("=========================================")
    print(' '*6 + "||   [1] Add an Entry       ||")
    print(' '*6 + "||   [2] Search an Entry    ||")
    print(' '*6 + "||   [3] Exit               ||")
    print("=========================================")

def main_menu():
    menu()
    while True:
        userPick = int(input("Pick a Function (1-3): "))
            
        if userPick == 1:
            user_add_entry()
            break

        if userPick == 2:
            user_find_entry()
            break
            
        # [7] Prompt User: Exit
        if userPick == 3:
            choice = input("Are you sure? (y/n): ")
            
            if choice == "y":
                print("Thank you for opening Yanji's Contact Tracing Directory!")
                exit()
            else:
                menu()
        
        else:
            print("Error! Invalid input. Press any key to continue...\n")

# [2] Initialize Dictionary: Contacts
contacts = {
    'John Doe':{'Age':'23', 'Address':'Manila', 'Phone':'09233456887'},
    'Sharon Lesley':{'Age':'22', 'Address':'Davao City', 'Phone':'09758832415'},
    'Arthur Gabriel':{'Age':'19', 'Address':'Quezon City', 'Phone':'09233456887'},
    'Shane Tyson':{'Age':'24', 'Address':'Cebu City', 'Phone':'09233456887'}
}
# [3] Ask User Entry
def user_add_entry():
    print("=========================================")
    print(' '*6 + "||       ADD AN ENTRY       ||")
    print("=========================================")
    print()

    name = input("Full Name: ")
# [4] Store User Input
    name = {}
    name['Age'] = (input("Age: "))
    name['Address'] = input("Address: ")
    name['Phone'] = (input("Phone Number: "))
    contacts.update(name)

    print("Contact Saved!")
    main_menu()

# [5] Recall User Input        
def user_find_entry():
    print("=========================================")
    print(' '*6 + "||       FIND AN ENTRY      ||")
    print("=========================================")
    print()

    while True:
        userFind = input("Full Name: ")
        
# [6] Print User Input
        if userFind in contacts.keys():      #Contact Exists 
            findname = contacts.get(userFind)
            for info in findname, contacts:
                print("Age: "+ info['Age'])
                print("Address: "+info['Address'])
                print("Phone Number: "+info['Phone'])
                print()
                print("=========================================")
                main_menu()
        else:     # Contact does not exist
            print("This contact does not exist in the directory.")
            print()
            print("=========================================")


main_menu()