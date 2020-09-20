from flask import Flask, url_for, render_template, request

app = Flask(__name__)

def numberenter(number):
    number = input("Please enter a number :") 
    
    while number != "exit":
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        numset = set(number)
        lennum1 = len(numset - digits)
    
        if lennum1 > 0:
        
            print("Not Valid Input !!!")
            return numberenter(number)
    
        if 1 < int(number) < 3999:
            number = int(number)       
            num1 = number % 10
            num10 = ((number % 100) - num1)
            num100 = ((number % 1000) - (num10 + num1))
            num1000 = (number - (num100 + num10 + num1))

            bnum1000 = int(num1000 / 1000)
            bnum100 = int(num100 / 100)
            bnum10 = int(num10 / 10)
            bnum1 = int(num1 / 1)
        
            rn1 = ""
            rn2 = ""
            rn3 = ""
            rn4 = ""

            while bnum1000:
                rn1 = (bnum1000 * "M")
                break
    
            while bnum100:
                if bnum100 < 4:
                    rn2 = (bnum100 * "C")
                elif bnum100 == 4:
                    rn2 = "CD"
                elif 5 <= bnum100 < 9:
                    rn2 = "D" + ((bnum100 - 5) * "C")
                else:
                    rn2 = "CM"
                break
    
            while bnum10:
                if bnum10 < 4:
                    rn3 = (bnum10 * "X")
                elif bnum10 == 4:
                    rn3 = "XL"
                elif 5 <= bnum10 < 9:
                    rn3 = "L" + ((bnum10 - 5) * "X")
                else:
                    rn3 = "XC"
                break
            

            while bnum1:
                if bnum1 < 4:
                    rn4 = (bnum1 * "I")
                elif bnum1 == 4:
                    rn4 = "IV"
                elif 5 <= bnum1 < 9:
                    rn4 = "V" + ((bnum1 - 5) * "I")
                else:
                    rn4 = "IX"
                break
    
            rn = rn1 + rn2 + rn3 + rn4

            print(rn)
            return numberenter(number)
                
        else:
            print("Not Valid! Please enter a number between 1 and 3999, inclusively!!!")
            return numberenter(number)
        
print(numberenter(number))

@app.route("/")
def home():
    return render_template("index.html", developer_name = "E2011_Yahya")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' : 
    	number = request.form['number']
        return render_template("result.html", number_decimal=number)
    else : 
        return render_template("index.html")
 

@app.route("/result")
def numberenter(number):
    return render_template("result.html", number_roman = number)
    

if __name__ == '__main__':
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=80)