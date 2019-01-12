#Import dependencies
from flask import Flask
from flask import request
#Create instance of Flask App
app = Flask(__name__)
#Define Route
@app.route("/")
def index(name="Threehouse"):
    name=request.args.get("name", name)
    return "Hello from {}".format(name)

#Running and Controlling the script
if (__name__ =="__main__"):
    app.run(debug=True, port=80, host='0.0.0.0')