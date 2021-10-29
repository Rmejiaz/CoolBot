from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import time

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip


def get_answer(message):
    output = "---"
    return output

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
        bot_message = get_answer(user_message)
        bot_messages.append(bot_message)
        return render_template("chat.html", user = user_messages, bot = bot_messages)
    else:
        return render_template("chat.html", user = user_messages, bot = bot_messages)

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



if __name__ == "__main__":
    app.run(debug=True)