# from distutils.log import debug
from flask import Flask, render_template, url_for, redirect 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Support")
def support():
    return render_template("Support.html")

@app.route("/AboutUs")
def aboutus():
    return render_template("AboutUs.html")

@app.route("/ContactUs")
def contactus():
    return render_template("ContactUs.html")

@app.route("/Applications")
def applications():
    return render_template("applications.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
 app.run(debug=True, port=8000)