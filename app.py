# SnapWords
import random
from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "super secret key"

pre_k_words = ['a', 'and', 'away', 'big', 'blue', 'can', 'come',
    'down', 'find', 'for', 'funny', 'go', 'help', 'here', 'I', 'in', 'is', 'it',
    'jump', 'little', 'look', 'make', 'me', 'my', 'not', 'one', 'play', 'red', 'run',
    'said', 'see', 'the', 'three', 'to', 'two', 'up', 'we', 'where', 'yellow', 'you', 'pen', 'pin']

k_words = ['all', 'am', 'are', 'at', 'ate', 'be', 'black', 'brown', 'but',
    'came', 'did', 'do', 'eat', 'four', 'get', 'good', 'have', 'he', 'into', 'like',
    'must', 'new', 'no', 'now', 'on', 'our', 'out', 'please', 'pretty', 'ran', 'ride',
    'saw', 'say', 'she', 'so', 'soon', 'that', 'there', 'they', 'this', 'too',
    'under', 'want', 'was', 'well', 'went', 'what', 'white', 'who', 'will', 'with', 'yes']

winter_words = ['snowflake', 'snow', 'hill', 'sled','hat', 'boot', 'winter', 'warm','cold','ice']

@app.route('/')
def home():
    session["counter"]=0
    session["words"] = k_words;
    return render_template('home.html', words = session["words"], index = session["counter"])

@app.route('/shuffle', methods=['POST'])
def shuffle():
    temp = session["words"]
    random.shuffle(temp)
    session["words"] = temp
    return render_template('home.html', words = session["words"], index = session["counter"])

@app.route('/next', methods=['POST'])
def next():
    if session["counter"] == (len(session["words"]) - 1):
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template('home.html', words = session["words"], index = session["counter"])

@app.route('/back', methods=['POST'])
def back():
    if session["counter"] == 0:
        session["counter"] = len(session["words"]) - 1
    else:
        session["counter"] -= 1
    return render_template('home.html', words = session["words"], index = session["counter"])

@app.route('/prekwords', methods=['POST'])
def prekwords():
    session["counter"] = 0
    session["words"] = pre_k_words
    return render_template('home.html', words = session["words"], index = session["counter"])

@app.route('/kwords', methods=['POST'])
def kwords():
    session["counter"] = 0
    session["words"] = k_words
    return render_template('home.html', words = session["words"], index = session["counter"])

@app.route('/winterwords', methods=['POST'])
def winterwords():
    session["counter"] = 0
    session["words"] = winter_words
    return render_template('home.html', words = session["words"], index = session["counter"])