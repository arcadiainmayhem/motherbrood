
import time
from core.installationConstants import DEV_MODE
import serial
from swamp.panelConstants import PANEL_FRAME



class PanellinkManager:

    #called in main with port + baud
    def __init__(self ,  port , baudrate):
       #serial object
        self.ser = serial.Serial(timeout=0)
            
        self.ser.baudrate = baudrate
        self.ser.port = port


        self._buf = b""
        self.droppedFrames=0

     
    #open serial port     
    def open(self):
        try:
            self.ser.open()

            return True
        except Exception as e:
            print(f"[PANELLINKMANAGER] Cant open serial port because of {e}")
            return False

    def close(self):
        #closes serial port / destroy object
        if self.is_connected():
            #connected, so active, can close
            self.ser.close()
            self.isOpen = False
        else: 
            #not connected nothing at all
            print("[PANELLINKMANAGER] Closing Error")

    #define where a frame ends
    def poll(self):
        #check and early return
        if not  self.is_connected():
            return []

        self._buf += self.ser.read(self.ser.in_waiting or 0)
        lines = self._buf.split(b"\n")
        self._buf = lines.pop() #incomplete tail


        frames = []
        for line in lines:
            #parse through the incoming lines of bytes
            frame = self._parse(line)
            if frame is None:
                self.droppedFrames += 1
            else:
                frames.append(frame)

        return frames

    #reads one line and determine if valid frame or not
    def _parse(self, line):
        try:

            frame = {}

            #decode byte to string
            decoded = line.decode('utf-8').strip()
            parts = decoded.split(",") #split removes commas


            #guards      
            if parts[0] != "P":
                return None
            
            if len(parts) - 1 < len(PANEL_FRAME):
                return None
            
            for name, raw in zip(PANEL_FRAME , parts[1:]):
                cast = PANEL_FRAME[name]
                frame[name] = cast(raw)


                        
                     #return
            return frame

    
        except Exception as e:
            print(f"[PANELLINKMANAGER] Error as : {e}")
            return None

    def send(self):
        
        pass

    def is_connected(self):
        return self.ser is not None and self.ser.is_open

