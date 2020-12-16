from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
=======
@app.route('/')
def hello():
    return 'Hello World'

if __name__=='__main__':
   app.run(host='0.0.0.0', port=80)
>>>>>>> 8d342a4c8610e8e7231f41ea49ff7027ad5c7e26
