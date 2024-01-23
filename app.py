import requests
from flask import Flask, render_template, request, redirect, flash
from flask_migrate import Migrate, upgrade


app = Flask(__name__)
app.config.from_object("config.ConfigDebug")




@app.route("/", methods=["GET"])
def startPage():
    return render_template("baseTemplate.html")








if __name__ == '__main__':
    app.run(debug=True)