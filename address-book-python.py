"""This program is called Address Book Python which is our Lab
Activity # 1 : Application of Python List in Data Structures and Algorithm. """


def addContact():
    """ This function will work once the user choose the option 1.
     This function is for adding a contact to address book."""
    contactList = [] #where the contact details is stored
    print("Adding a contact....") #let the user know that they're adding a contact
    firstName = input("Enter the first name: ") #input for the first name of the contact
    contactList.append(firstName) #add the first name to contactList
    lastName = input("Enter the last name: ") #input for the last name of the contact
    contactList.append(lastName) #add the last name to contactList
    address = input("Enter the address: ") #input for the address of the contact
    contactList.append(address) #add the address to contactList
    contactNumber = input("Enter the contact number: ") #input for the number of the contact
    contactList.append(contactNumber) #add the contact number to contactList
    ''' The codes below will save the entered details of the contact to a txt file.'''
    txtFile1 = open('AddressBook.txt', 'r') #open the txt file to read mode
    entries = txtFile1.readlines() #read the information per line in txt file
    entryNum = len(entries) #gives the count of lines in txt file
    '''This is an if-else statement, therefore the txt file are only allowed 
    to have 50 entries before they are maxed out and contacts cannot be stored.'''
    if entryNum != 50: #limit the entry to 50
        txtFile = open('AddressBook.txt', 'a') #open the txt file in append mode
        txtFile.write(f"{contactList}\n") #add the contact details to txt file
        txtFile.close() #close the txt file
        print(f"Successfully added contact! Your entry number is {entryNum + 1}.") #let the user know the contact is added
    else:
        print("Sorry, you can't add another contact! The address book is now full.") #let the user know the contact can't be added anymore
    txtFile1.close() #close the txt file


def editContact():
    """This function will work once the user choose the option 2.
    This will help the user edit the contact details they want to change."""
    print("Editing a contact...") #let the user know they're editing a contact
    entryNumber = int((input("Enter the entry number of "
                             "the contact you want to edit: "))) #input for the entry number of the contact they want to edit
    txtFile = open('AddressBook.txt', 'r') #open the txt file in read mode
    lines = txtFile.readlines() #read the information per line in txt file
    txtFile.close() #close the txt file
    if (entryNumber <= len(lines)): # this will proceed if the entry number the user entered is in the txt file
        deleteContact = input("Are you you want to edit this contact? y/n: ") # making sure if the user really wanted to edit the contact
        if deleteContact.lower() == 'y': #the codes below will proceed if the user entered 'y'
            editContact = [] #list where the updated details will be stored
            print("Editing a contact....") #let the user know they're editing a contact
            firstName = input("Update the first name: ") #input for the updated first name
            editContact.append(firstName) #add the updated first name to editContact list
            lastName = input("Update the last name: ") #input for the updated last name
            editContact.append(lastName) #add the updated last name to editContact list
            address = input("Update the address: ") #input for the updated address
            editContact.append(address) #add the updated address to editContact list
            contactNumber = input("Update the contact number: ") #input for the updated contact number
            editContact.append(contactNumber) #add the updated contact number in editContact list
            lines[entryNumber - 1] = (f"{editContact}\n") #the updated contact details will now be stored in the entry(line) number,
                                                            # they entered, in txt file
            txtFile = open('AddressBook.txt', 'w') #open the txt file in write mode
            for line in lines: # loop per line in txt file
                txtFile.write(line) # will rewrite all the lines in the txt file along the with updated contact details
            print("Contact successfully edited.") #let the user know the contact is sucessfully edited.
        elif deleteContact.lower() == 'n': # the code below will proceed if the user entered 'n'
            print("Contact will not be edited.")
    else: #if the user entered a wrong(not existing) entry number the code below will proceed
                print("Entry", entryNumber, "not found.") #let the user know the entry number they entered doesn't exist
    txtFile.close() #close the txt file


def deleteContact():
    """This function will work if the user chooses the option 3.
    This will let the user delete a saved contact."""
    print("Deleting a contact...") #let the user know they're deleting a contact
    entryNumber = int((input("Enter the entry number of the contact you want to delete: "))) #input for the entry number of the contact they want to edit
    txtFile = open('AddressBook.txt', 'r') #open the txt file in read mode
    lines = txtFile.readlines() #read the information per line in txt file
    txtFile.close() #close the txt file
    if (entryNumber <= len(lines)): # this will proceed if the entry number the user entered is in the txt file
        deleteContact = input("Are you you want to delete this contact? y/n: ") # making sure if the user really wanted to delete the contact
        if deleteContact.lower() == 'y': #the codes below will proceed if the user entered 'y'
            del lines[entryNumber - 1] #the contact will now be deleted in the entry(line) number, the user entered, in txt file
            txtFile = open('AddressBook.txt', 'w') #open the txt file in write mode
            for line in lines: #loop per line in txt file
                txtFile.write(line) # twill rewrite all the the lines in the txt file except for the deleted line
            print("Contact successfully deleted.") #let the user know the contact is deleted
        elif deleteContact.lower() == 'n':
            print("Contact will not be deleted.") #let the user know the contact will not be deleted
    else:
        print("Entry", entryNumber, "not found.") #let the user know the entry number they entered doesn't exist
    txtFile.close() #close the txt file


def viewContacts():
    """This will work once the user choose the option 4.
    This will just display all of the saved contacts."""
    viewContacts = [] #where the contacts will be stored
    entryCount = 0 #this will add count as the for loop go through every line in txt file
    print("Displaying contacts...\n") #let the user know it will the display all the contacts
    txtFile = open('AddressBook.txt', 'r') #open the txt in read mode
    for line in txtFile: #loop the the txt file per line to get information
        viewContacts = eval(line) #evaluate the details found per line
        entryCount = entryCount + 1 #once a line has been identified, entryCount will be incremented by 1
        print(f"Entry No.:     ",entryCount,
              "\nFirst Name:    ", viewContacts[0],
              "\nLast Name:     ", viewContacts[1],
              "\nAddress:       ", viewContacts[2],
              "\nContact Number:", viewContacts[3],"\n") #this will get and print the details in the lines found per index
    txtFile.close() #close the txt file


def searchContact():
    """This function will work once the user choose the option 5.
    This will help the user to search for a contact."""
    contactDetails = [] #where the contact details searched is stored
    print("Searching for a contact...") #let the user know they are searching for contact
    search = input("Enter the contact's info such as first name, last name, address, "
                   "or contact number: ") #input for the contact they want to find
    txtFile = open('AddressBook.txt', 'r') #open the txt file in read mode
    found = False #used in the if statement below to know if the contact has been found
    for line in txtFile: #will search every details of every line in txt file
        if search in line: #the codes below will proceed if the contact has been found in txt file
            contactDetails = eval(line) #evaluate the details found per line in txt file
            print("Contact/s found in the address book: ") #let the user know the contact has been found
            print(f"First Name:",contactDetails[0],
                  "\nLast Name:",contactDetails[1],
                  "\nAddress:",contactDetails[2],
                  "\nContact Number:",
                  contactDetails[3],"\n") #this will print details of the contact/s that has been found
            found = True #let the program know the contact has been found
    if found == False: #the code below will proceed if the contact is not found in the txt file
        print("The contact is not found!") #let the user know the contact is not found
    txtFile.close() #close the txt file


def mainMenu():
    """This function will just let the program run and let the user know it is an Address Book program.
    The user will also be given an options what they want to do in the Address Book."""
    while True: #while loop will let the program run infinitely unless the user decided to exit
        print("-------------------Address Book----------------------") #let user know it is a address book
        choice = (input(
            "What would you like to do?"
            "\n 1 - Add Contact\n 2 - Edit\n 3 - Delete Contact"
            "\n 4 - View Contacts\n 5 - Search Address Book\n 6 - Exit"
            "\n Choose an option: ")) # input for the option the user want to choose
        if choice == '1':
            #1. Add contact
            addContact() # prompt the user for the first name, last name, address, and contact number.
        elif choice == '2':
            #2. Edit contact
                editContact() # prompt the user for the entry number he wants to edit.
        elif choice == '3':
            #3. Delete contact
            deleteContact() # prompt the user for the entry number he wants to delete.
            viewContacts() # additional so that the user will know that the contact is now deleted and
                           # let him know the updated entry numbers
        elif choice == '4':
            #4. View contacts
            viewContacts() # display all the entries
        elif choice == '5':
            #5. Search Address Book
            searchContact() # prompt the user to search the address book (a) by first name, (b) by last name,
                                        # (c) by address, (d) by contact number.
        elif choice == '6':
                print("Exiting the program...") #let the user know the program is closed
                break #break the while loop
        else:
            print("Invalid input! Try again.") #let the user know they entered a wrong input


mainMenu() # run the program