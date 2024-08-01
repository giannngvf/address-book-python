# Address Book Python

## Overview

The Address Book Python program is a lab activity focused on the application of Python lists in data structures and algorithms. It allows users to manage contacts by adding, editing, deleting, viewing, and searching for entries in an address book.

## Features

- **Add Contact**: Allows users to add new contacts with first name, last name, address, and contact number.
- **Edit Contact**: Enables users to update details of an existing contact.
- **Delete Contact**: Provides functionality to remove a contact from the address book.
- **View Contacts**: Displays all saved contacts.
- **Search Contacts**: Searches for contacts by first name, last name, address, or contact number.

## File Structure

- **AddressBook.txt**: This file stores the contact details. Each entry is stored as a list in a new line.

## How to Run

1. Ensure you have Python installed on your system.
2. Save the script provided in a `.py` file (e.g., `address_book.py`).
3. Run the script using the command: `python address_book.py`.

## Code Description

### Functions

- `addContact()`: Adds a new contact to the address book. Limits the number of entries to 50.
- `editContact()`: Edits an existing contact based on the entry number.
- `deleteContact()`: Deletes a contact based on the entry number.
- `viewContacts()`: Displays all contacts in the address book.
- `searchContact()`: Searches for contacts based on user input.
- `mainMenu()`: Provides the main menu interface for user interactions.

### Author's Note
This is the very first program I developed that I’m truly proud of. It was very challenging for me, so I really did a lot of research, especially on how can it save contacts and how can it also retrieve the users' information.

### Example Usage

```plaintext
-------------------Address Book----------------------
What would you like to do?
 1 - Add Contact
 2 - Edit
 3 - Delete Contact
 4 - View Contacts
 5 - Search Address Book
 6 - Exit
 Choose an option: 
