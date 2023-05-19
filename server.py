from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:input>')
def say_this(input):
    return "Hi " + input

@app.route('/repeat/<string:input>/<int:num>')
def repeat(input, num):
    return input * num

if __name__=="__main__":
    app.run(debug=True)


