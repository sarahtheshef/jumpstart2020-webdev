# app.py

from flask import Flask, render_template, redirect, url_for, jsonify
import poembot

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi, you've reached 2020. I'm not here right now. Leave a message maybe? Good luck."

@app.route('/poem')
def poem():
    poem = poembot.generate_poem()
    return render_template('poem.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)
