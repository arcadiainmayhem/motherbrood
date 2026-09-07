
import subprocess , time
from pathlib import Path
from core.installationConstants import *
from pythonosc.udp_client import SimpleUDPClient

LOOPBACK_IP = "127.0.0.1"

class PuredataManager:



    def __init__(self , patch_path , audio_device , osc_port):


        self.patch_path = str(patch_path)

        #check if it exists
        if not Path(patch_path).exists():
            raise FileNotFoundError(f"Patch not found {patch_path}")

        self.audio_device = audio_device



        self.osc_port = osc_port

        self.process = None

        #start Client
        self.osc_client = SimpleUDPClient(LOOPBACK_IP,osc_port)


    #start swampbed - puredata
    #have to run the patch FROM the console to start + turn on DSP 
    def start(self):

        if DEV_MODE:
            print("[PUREDATAMANAGER] DEV MODE - Assuming Plugdata is open")
            return True

        #configuration of PD
        pdconfiguration = [
            "pd","-nogui", "-alsa", '-noadc',
            "-audiooutdev", self.audio_device ,"-channels","2","-r","44100",
            self.patch_path
        ]

        try:
            #starts another program - tetlls OS to launch it
            self.process = subprocess.Popen(pdconfiguration , stderr=subprocess.PIPE)

            time.sleep(1)

  
            if self.process.poll() is not None:
                #died on startup
                errors = self.process.stderr.read().decode() #.read() returns bytes and .decode() turns it into string
                print("[PUREDATAMANAGER] PD Died : {errors}")
            
                self.process = None
                return False
            #process is running
            return True
        
        except FileNotFoundError as e:
            
            print(f"[PUREDATAMANAGER] PUREDATA Unable to run because of : {e}")

            return False

    def stop(self):
        if self.process is None:
            return
        self.process.terminate()
        try:
            self.process.wait(timeout = 3)
        except subprocess.TimeoutExpired:

            self.process.kill()
            self.process.wait()

        self.process = None

    def restart(self):
        self.stop()
        return self.start()



    def is_running(self):
        return self.process is not None and self.process.poll() is None


    def send(self, address , value):
        self.osc_client.send_message(address, value)