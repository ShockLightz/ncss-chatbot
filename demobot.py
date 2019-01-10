# Import flask
from flask import Flask, request
import random

# Create your app (web server)
app = Flask(__name__)

@app.route('/emote', methods=['GET', 'POST'])
def emote():
    emotes = ['(✿◠‿◠)', '≧◡≦', '(▰˘◡˘▰)', '(●´ω｀●)', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧', 
              '（ミ￣ー￣ミ）', '(づ｡◕‿‿◕｡)づ', '✌.ʕʘ‿ʘʔ.✌', '◎[▪‿▪]◎']
    return random.choice(emotes)

@app.route('/table-flip', methods=['GET', 'POST'])
def table_flip():
    return '(╯°□°）╯︵ ┻━┻'

if __name__ == '__main__':
    # Start the web server!
    app.run()