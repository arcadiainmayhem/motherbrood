


from flask import Flask

#creating flask application
app = Flask(__name__)


#what should it be doing
#check current cicadas + params
#check messages to PD
#check panel messages to PD

#installation states
#Current LED


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"