from flask import Flask, render_template, request

app = Flask(__name__)

def convert(decimal_num):
<<<<<<< HEAD
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4:'IV', 1: 'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman    

@app.route("/",)
def index():
    return render_template('index.html', developer_name = 'E2011_Yahya', not_valid = False)
    
@app.route("/", methods = ['POST'])
def index_post():
    if request.method == 'POST':
        x = request.form['number']
        if not x.isdecimal():
            return render_template('index.html', developer_name = 'E2011_Yahya', not_valid = True )
        
        number = int(x)
        if not (0 < number < 4000):
            return render_template('index.html', developer_name = 'E2011_Yahya',not_valid = True)
        
        return render_template("result.html", developer_name = 'E2011_Yahya', number_decimal = x, number_roman = convert(number) )

    

if __name__ == '__main__':
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=80)
=======
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i)
        decimal_num %= i
    return num_to_roman

@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', developer_name='Serdar', not_valid=False)

@app.route('/', methods=['POST'])
def main_post():
    alpha = request.form['number']
    if not alpha.isdecimal():
        return render_template('index.html', developer_name='Serdar', not_valid=True)

    number = int(alpha)
    if not 0 < number < 4000:
        return render_template('index.html', developer_name='Serdar', not_valid=True)

    return render_template('result.html', number_decimal = number , number_roman= convert(number), developer_name='Serdar')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)







>>>>>>> 8d342a4c8610e8e7231f41ea49ff7027ad5c7e26
