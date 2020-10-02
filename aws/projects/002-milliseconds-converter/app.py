from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route("/",)
#def index():
#    return render_template('index.html', developer_name = 'E2014_Devin', not_valid = False)
    
@app.route("/", methods = ['GET', 'POST'])
def index_post():

    if request.method == 'GET':
        return render_template('index.html', developer_name = 'E2011Yahya', not_valid = False)

    else:
        number = request.form['number']
        
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        numset = set(number)
        lennum1 = len(numset - digits)
        if lennum1 > 0:
            return render_template('index.html', developer_name = 'E2011Yahya', not_valid = True )

        number = int(number)
        if number <= 0:
            return render_template('index.html', developer_name = 'E2014Yahya', not_valid = True)
    
        else:
            resulted = 0
            number = int(number)       
            numhour = number // 3600000
            nummin = (number - (numhour * 3600000)) // 60000
            numsecond = (number - ((numhour * 3600000) + (nummin * 60000))) // 1000
            
            def printouter(number):
                if numhour == 0 and numsecond == 0 and nummin == 0:
                    return f"{number} milisecond/s"
                elif nummin == 0 and numsecond== 0:
                    return f"{numhour} hour/s"
                elif numhour == 0 and numsecond == 0:
                    return f"{nummin} minute/s"
                elif numhour == 0 and nummin == 0:
                    return f"{numsecond} second/s" 
                elif numhour == 0:
                    return f"{nummin} minute/s " + f"{numsecond} second/s"
                elif numsecond == 0:
                    return f"{numhour} hour/s " + f"{numsecond} minute/s"
                elif nummin == 0:
                    return f"{numhour} hour/s " + f"{numsecond} second/s"
                else:           
                    return f"{numhour} hour/s " + f"{nummin} minute/s " + f"{numsecond} second/s"

            return render_template("result.html", developer_name = 'E2011ahya', milliseconds = number, result = printouter(number))
            
if __name__ == '__main__':
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=80)