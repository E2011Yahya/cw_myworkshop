name = input("Please enter your full name : ")
nums = "1234567890"

lowername = set(name.lower())
listname = list(lowername)
setnums = set(nums)
listnums = list(setnums)
secretkey = []
for i in listname[0:3]:
    if i == " " :
        letter = listname[4]
        secretkey.append(letter)
    else:
        secretkey.append(i) 


for i in listnums[0:4]:
    secretkey.append(i)

password = ""
for i in secretkey:
    password += i


print(password)