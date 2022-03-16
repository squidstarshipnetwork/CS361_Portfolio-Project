from os import system, name
from os.path import exists
from time import sleep

choice = 1
interim_list = []
list = []

def print_menu():
    print("Welcome to the Catalog Menu!\n Please select from the following options:\n")
    print("1.  Import List\n")
    print("2.  Export List\n")
    print("3.  Add an Item\n")
    print("4.  Delete an Item\n")
    print("5.  Clear List\n")
    print("Press 0 to Quit\n")

def clear():
    #found in an article from stackoverflow
    #this makes this command possible to run on multiple environments and platforms
    #specifically, Windows systems (nt) and Unix-like systems.
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def print_items():
    print("Here is your list:\n")
    if len(list):
        print(*list, sep = "\n")
        print("\n")
    else:
        print("No items in list. . .\n\n")

def add_item():
    raw_item = input("Please enter an item: ")
    trimmed_item = raw_item.strip()
    list.append(trimmed_item)

def import_list(list):

        #Ask for encrypted file
        print("Is this file encrypted?\n")
        decr_choice = input(": ")

        #if encrypted, write to instructions and read response after waiting
        if decr_choice == "Y":
            with open("instructions.txt", "w") as instructions:
                instructions.write("N\nD")
            #sleep statement to make sure time is given for the instruction file to be written to.
            #also accounts for time needed to process the request.
            sleep(5)

            with open("d_response.txt", "r") as import_file:
                for line in import_file:
                    list.append(line.replace("\n", ""))

        elif decr_choice == "N":

            with open("backup.txt", "r") as import_file:
                for line in import_file:
                    list.append(line.replace("\n", ""))

def export_list():
    print("writing to file . . .")
    encr = open("instructions.txt", "w")
    sleep(2)
    print("Do you wish to encrypt?\n")
    en_choice = input(": ")
    if en_choice == 'Y':
        with open("e_request.txt", "w") as export_file:
            for line in list:
                export_file.write(line + "\n")
        encr.write("Y\nE")
        encr.close()
        #safety sleep to wait for a the microservice to encrypt the file
        sleep(5)
    else:
        #Create the backup text file
        encr.write("N\nD")
        with open("backup.txt", "w+") as backup_file:
            for element in list:
                backup_file.write(element + "\n")
        encr.close()
        sleep(3)

def delete_item():
    raw_item = input("Let's delete an item: ")
    trimmed_item = raw_item.strip()
    for elements in list:
        if elements == trimmed_item:
            list.remove(trimmed_item)
            break

def clear_list():
    list.clear()

def quit_menu():
    print("Goodbye . . . \n")

while choice != 0:
    clear()

    #Access instructions.txt and clear the contents of the List
    #Safety measure in case of user not processing commands fast enough
    instr = open("instructions.txt", 'r+')
    instr.truncate(0)

    print_items()

    print_menu()
    choice = int(input(": "))

    if choice == 1:
        import_list(list)

    elif choice == 2:
        export_list()

    elif choice == 3:
        add_item()

    elif choice == 4:
        delete_item()

    elif choice == 5:
        clear_list()

    elif choice == 0:
        quit_menu()

    else:
        print("Sorry, I don't recognize that command. . .\n")
