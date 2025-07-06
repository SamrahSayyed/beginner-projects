# We use the library re here for validating the contact number entered by the user.
import re
names = []  
contact_numbers = []

while True:  
    
    print("1. View Contact Book\n2. Add numbers in the Contact Book\n3. Delete number from the Contact Book\n4.Search a Contact\n5.Exit Contact Book")
    try:
       option = int(input("Choose any option from 1 to 5: "))
       if option not in [1, 2, 3, 4, 5]:                   #if the input is not from 1-5 (required input), the user is asked to choose any option between 1 and 5.
        print("Enter an option between 1 and 5")
        continue
    except ValueError:                                     #if the value entered by the user is anything except an integer, it is considered invalid.
       print("Enter a valid number.")
       continue

    if (option == 1):
      if not names:                        #if nothing is present in the list 'names'.
          print("No contacts yet!")
      else:
          print("Your contacts are: ")
          print("Name".ljust(20)+"Contact")            #.ljust() is used to ensure proper alignment and spacing between the name and the contact of the person, in a tabular format.
          for i in range(len(names)):
            print(names[i].ljust(20)+contact_numbers[i])    


    elif (option == 2):
        
        try:
           nums = int(input("How many contacts do you need to add? "))
           for i in range(nums):      #asks the user to input contacts repeatedly until required
             while True:
              name = input("Name: ")
              contact = (input("Contact: "))   
              if (re.fullmatch('[6-9][0-9]{9}',contact)):                 #using the 're' library, this checks the contact number, the first digit of the number should be between 6 and 9, the next 9 numbers should be between 0 and 9, hence, only it allows 10 digit number if and only if all the conditions are met.
               names.append(name)                             #the name is added to the end of the list 'name'
               contact_numbers.append(contact)                #the contact is added to the end of the list 'contact_numbers'
               print("Contact Numbers added successfully.")
               break
              else:
               print("Enter a valid contact number.")               #if the contact number does not meet the required conditions, user is prompted to add a valid contact number.
        except ValueError:
            print("Enter a valid number.")                          #this is prompted if the user enters any other value except an integer.
    

    elif (option == 3):
        delete_name = input("Enter the name of the contact you want to delete: ").strip()              #.strip() is used to filter out any unwanted spaces the user may enter after the name, like 'samrah '
        if delete_name not in names:
          print("Contact not found.")
        else:
          index = names.index(delete_name)
          del names[index]
          del contact_numbers[index]
          print("Contact Numbers deleted.")

    elif (option ==  4):
          search_name = input("Enter the name of the contact you want to search: ").strip().lower()          #.lower() is used to switch all the letters in the name to lowercase

          lower_names = [n.lower() for n in names]                                                           #the name switched is saved in this variable lower_names
          
          if not search_name:
            print("You didn't enter any name.")                                                              #this is prompted if user didn't enter anything as input
            
          elif search_name in lower_names:
            search_index = lower_names.index(search_name)                                                   #saves the index of the name searched
            contact_number = contact_numbers[search_index]                                                  #saves the index of the contact searched
            print("\nSearch Result:")
            print("Name:".ljust(10) + names[search_index])
            print("Contact:".ljust(10) + contact_number)
          else:
             print("No records found.")


    else:
       print("Exiting Contact Book.")
       break                                                                                              #exits the contact book
