from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Pocetna strana"

@app.route("/studio1")
def studio1():
    return "Studio 1"

@app.route("/studio2")
def studio2():
    return "studio2"

@app.route("/studio3")
def studio3():
    return "studio3"

@app.route("/studio4")
def studio4():
    return "studio4"

@app.route("/apartman5")
def apartman5():
    return "apartman5"

@app.route("/apartman6")
def apartman6():
    return "apartman6"

@app.route("/virtuelnaSetnja")
def virtuelnaSetnja():
    return "virtuelnaSetnja"

@app.route("/kutak")
def kutak():
    return "kutak"

if __name__ == '__main__':
    app.run()