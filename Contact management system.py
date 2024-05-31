contacts = {}

def add_contact():
  name = input("Enter name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email address: ")
  contacts[name] = {"phone": phone, "email": email}
  print("Contact added successfully!")

def view_contacts():
  if not contacts:
    print("No contacts saved.")
  else:
    for name, info in contacts.items():
      print(f"Name: {name}")
      print(f"Phone: {info['phone']}")
      print(f"Email: {info['email']}")
      print("-" * 20)

def edit_contact():
  name = input("Enter name of contact to edit: ")
  if name in contacts:
    print("1. Edit phone number")
    print("2. Edit email address")
    choice = input("Enter your choice: ")
    if choice == '1':
      new_phone = input("Enter new phone number: ")
      contacts[name]["phone"] = new_phone
      print("Phone number updated!")
    elif choice == '2':
      new_email = input("Enter new email address: ")
      contacts[name]["email"] = new_email
      print("Email address updated!")
    else:
      print("Invalid choice.")
  else:
    print("Contact not found.")

def delete_contact():
  name = input("Enter name of contact to delete: ")
  if name in contacts:
    del contacts[name]
    print("Contact deleted!")
  else:
    print("Contact not found.")

while True:
  print("\nContact Management System")
  print("1. Add contact")
  print("2. View contacts")
  print("3. Edit contact")
  print("4. Delete contact")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    add_contact()
  elif choice == '2':
    view_contacts()
  elif choice == '3':
    edit_contact()
  elif choice == '4':
    delete_contact()
  elif choice == '5':
    break
  else:
    print("Invalid choice.")