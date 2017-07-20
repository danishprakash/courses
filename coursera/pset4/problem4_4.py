import os
import csv

phones = []

def show_phones():
    #print('printing..')
    header = ['Name', 'Phone Number ']
    show_phone(header, "")
    index = 1;
    for phone in phones:
        show_phone(phone, index)
        index += 1
    print()

def load_phone_list():
    if os.access("myphones.csv", os.F_OK):
        reader = open("myphones.csv")
        for item in csv.reader(reader):
            phones.append(item)
        reader.close()
    

def save_phone_list():
    dbase = open("myphones.csv", 'w', newline='')
    for item in phones:
        csv.writer(dbase).writerow(item)
    dbase.close()

def show_phone(phone, index):
    print("{0:>3}  {1:<20}  {2:>16}".format(index, phone[0], phone[1]))


def create_phone():
    #print('Opening..')
    print('Enter the data for a new phone:')
    name = input('Enter name: ')
    number = input('Enter phone number: ')
    phone = [name, number]
    phones.append(phone)

def proper_menu_choice(which):
    if not which.isdigit():
        print ("'" + which + "' needs to be the number of a phone!")
        return False

    which = int(which)

    if which < 1 or which > len(phones):
        print ("'" + str(which) + "' needs to be the number of a phone!")
        return False

    return True

def delete_phone(which):
    #print('Deleting...')
    if not proper_menu_choice(which):
        return
    which = int(which)

    del phones[which-1]
    print( "Deleted phone #", which) 

def reorder_phones():
    global phones
    phones.sort()


def edit_phone(which):
    #print('Editing...')
    if not proper_menu_choice(which):
        return
    which = int(which)
    phone = phones[which-1]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    #print('Change name for ' + str(phone[0]) + '?')
    newname = input('Enter phone name to change or press return: ')
    if newname == '':
        newname = phone[0]

    #print(str(phone[1]))
    newnumber = input('Enter new phone number to change or press return: ')
    if newnumber == '':
        newnumber = phone[1]

    phone = [newname, newnumber]
    phones[which-1] = phone
    #print(phone[which][1])

"""
def menu_choice():
    print('Choose one of the following options:')
    print('    s) Show\n    n) New\n    d) Delete\n    e) Edit\n    r) Reorder\n    q) Quit')
    choice = input('Choice: ')
    if choice.lower() in ['s', 'n', 'd', 'e', 'q', 'r']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None
"""

def menu_choice():
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   s) Show")
    print("   n) New")
    print("   d) Delete")
    print("   e) Edit")
    print("   r) Reorder")	
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in ['n','d', 's','e', 'q', 'r']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None

def main_loop():
    load_phone_list()

    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == 'n':
            create_phone()
        elif choice == 'd':
            which = input("Which item do you want to delete? ")
            print("which is ", which)
            delete_phone(which)
        elif choice == 's':
            show_phones()
        elif choice == 'r':
            phones.sort()
        elif choice == 'e':
            which = input("Which item do you want to edit? ")
            print("which is ", which)
            edit_phone(which)
        else:
            print("Invalid choice.")

    save_phone_list()


if __name__ == '__main__':
    main_loop()
