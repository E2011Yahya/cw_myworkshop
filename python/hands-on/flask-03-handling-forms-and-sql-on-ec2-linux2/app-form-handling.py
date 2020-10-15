from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name = 'E2011-Yahya')

@app.route('/greet')  
def greet():
    return render_template('greet.html')  

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        return render_template('secure.html', user=user_name)
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
  # app.run(host='0.0.0.0', port=80)