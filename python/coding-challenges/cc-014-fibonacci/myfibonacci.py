mynum = int(input("How many fibonacci numbers would you like to generate?"))
mynum = int(input("How many fibonacci numbers would you like to generate?"))

def fibo(int):
    num_list = range(mynum)
    my_list = []
    x, y  = 0, 1 
   
    for i in num_list:
        x, y = y, x + y
              
        my_list.append(x)
    
    print(my_list)

fibo(mynum)




