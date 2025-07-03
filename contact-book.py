import re
names = []
contact_numbers = []

while True:
    
    print("1. View Contact Book\n2. Add numbers in the Contact Book\n3. Delete number from the Contact Book\n4.Search a Contact\n5.Exit Contact Book")
    try:
       option = int(input("Choose any option from 1 to 5: "))
       if option not in [1, 2, 3, 4, 5]:
        print("Enter an option between 1 and 5")
        continue
    except ValueError:
       print("Enter a valid number.")
       continue

    if (option == 1):
      if not names:
          print("No contacts yet!")
      else:
          print("Your contacts are: ")
          print("Name".ljust(20)+"Contact")
          for i in range(len(names)):
            print(names[i].ljust(20)+contact_numbers[i])


    elif (option == 2):
        
        try:
           nums = int(input("How many contacts do you need to add? "))
           for i in range(nums):
             while True:
              name = input("Name: ")
              contact = (input("Contact: "))   
              if (re.fullmatch('[6-9][0-9]{9}',contact)):
               names.append(name)
               contact_numbers.append(contact)
               print("Contact Numbers added successfully.")
               break
              else:
               print("Enter a valid contact number.")
        except ValueError:
            print("Enter a valid number.")
    

    elif (option == 3):
        delete_name = input("Enter the name of the contact you want to delete: ").strip()
        if delete_name not in names:
          print("Contact not found.")
        else:
          index = names.index(delete_name)
          del names[index]
          del contact_numbers[index]
          print("Contact Numbers deleted.")

    elif (option ==  4):
          search_name = input("Enter the name of the contact you want to search: ").strip().lower()

          lower_names = [n.lower() for n in names]
          
          if not search_name:
            print("You didn't enter any name.")
            
          elif search_name in lower_names:
            search_index = lower_names.index(search_name)
            contact_number = contact_numbers[search_index]
            print("\nSearch Result:")
            print("Name:".ljust(10) + names[search_index])
            print("Contact:".ljust(10) + contact_number)
          else:
             print("No records found.")


    else:
       print("Exiting Contact Book.")
       break