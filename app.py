import random

from random_username.generate import generate_username

from flask_socketio import SocketIO
from flask import Flask, \
    render_template, request


app = Flask(__name__)
app.config["DEBUG"] = False

socketio = SocketIO(app)

def usercolor():
    return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])


@socketio.on("sendMessage")
def msg_handler(message):
    socketio.emit("newMessage", message, broadcast=True)

@app.route("/")
def index():
    return render_template("index.html", username=generate_username()[0], color=usercolor())


if __name__ == "__main__":
    socketio.run(app, port=3003)
