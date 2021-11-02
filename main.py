from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import time
from utils import chat_response
import tensorflow as tf
import json

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip


model = tf.keras.models.load_model('model1.h5')
intents = json.loads(open('intents.json').read())

@app.route("/")
def home():
    user_messages.clear()
    bot_messages.clear()
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

user_messages = []
bot_messages = []
@app.route("/chat", methods = ["POST", "GET"])
def chat():
    if request.method == "POST":
        user_message = request.form["nm"]
        user_messages.append(user_message)
        bot_message = chat_response(user_message, model, intents)
        bot_messages.append(bot_message)
        return render_template("chat.html", user = user_messages, bot = bot_messages)
    else:
        return render_template("chat.html", user = user_messages, bot = bot_messages)





if __name__ == "__main__":
    app.run(debug=True)
