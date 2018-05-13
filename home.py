from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
   return "<center> <h1> Railway Enquiry System </h1> </center>"
app.run()
@app.route("/Live Status")
def status():
   return "<center> <h1> Status </h1> </center>"
app.run()