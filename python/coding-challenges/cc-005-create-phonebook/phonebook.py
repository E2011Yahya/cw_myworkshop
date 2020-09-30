

book = {}
select = input("Welcome to the phonebook application \n 1. Find phone number \n 2. Insert a phone number \n 3. Delete a person from the phonebook \n 4. Terminate \n Select operation on Phonebook App (1/2/3) :")

while 0 < int(select) < 4 :
    
    if int(select) == 1:
        name = input("Please enter a name: ")
            
        if name in book :
            x = book[name]
            print(x)
        else:
            print(f"{name} is not in the address book") 
        

    if int(select) == 2:
        name = input("Insert name of the person : ")
        num = input("Insert phone number of the person: ")
        book[name] = num
        print(f"Phone number of {name} is inserted into the phonebook")
        print(book)

    if int(select) == 3:
        name = input("Whom to delete from phonebook : ")
            
        if name in book :
            book.pop(name)
            print(f"{name} is deleted from the phonebook")

        else:
            print(f"{name} is not in the address book")




    select = input("Welcome to the phonebook application \n 1. Find phone number \n 2. Insert a phone number \n 3. Delete a person from the phonebook \n 4. Terminate \n Select operation on Phonebook App (1/2/3) :")    
    
print("Exiting Phonebook")    
       