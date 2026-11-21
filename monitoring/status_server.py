from core.installationConstants import STATUS_SERVER_PORT
from flask import Flask , render_template , redirect , jsonify
from monitoring.status_logger import get_snapshot
import threading
import time


#creating flask application
app = Flask(__name__)


#what should it be doing

#check current cicadas + params
#check messages to PD

#check panel messages to PD
#current button presses

#current gesture

#installation states

#Current LED


@app.route("/")
def index():
    return print(f"[STATUS SERVER LIVE]")




@app.route("/status")
def check_status():
    return jsonify(get_snapshot())



def _run():
    app.run(host = "0.0.0.0" , 
            port = STATUS_SERVER_PORT , 
            debug = False ,
            use_reloader = False)

def start_status_server():
    server_thread = threading.Thread(target= _run,
                     daemon= True,
                     )
    server_thread.start()