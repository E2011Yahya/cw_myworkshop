list_string = list(input("Please enter a string : "))
vowels = ["a", "e", "i", "o", "u"]

a = len(list_string)
x = 0
for i in list_string:
    x += 1
    if x < a :
        if i in vowels: 
            if list_string[x] in vowels:   
                print("Positive")
                break
    else:        
        print("Negative")
       
        

        




