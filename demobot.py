# Import flask
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)

# When people visit the home page '/' use the hello_world function
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'

# When people visit the ncss page /ncss use the hello_world function
@app.route('/ncss', methods=['GET', 'POST'])
def ncss():
    return '<h1>NCSS</h1>'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = request.values.get('text', methods=['GET', 'POST'])
    return f'hi {name}'

@app.route('/weather', methods=['GET', 'POST'])
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