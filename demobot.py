# Import flask
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)

# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# When people visit the ncss page /ncss use the hello_world function
@app.route('/ncss')
def ncss():
    return '<h1>NCSS</h1>'

@app.route('/greet')
def greet():
    name = request.values.get('text')
    return f'hi {name}'

@app.route('/weather')
def weather():
    temp = int(request.values.get('temp'))
    cond = 'nice'
    if temp > 30:
        cond = 'hot'
    elif temp < 15:
        cond = 'cold'
    return f'it\'s a {cond} day'

if __name__ == '__main__':
    # Start the web server!
    app.run()