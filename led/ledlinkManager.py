


import time
import serial
from core.installationConstants import OPEN_LED_SERIAL , DEV_MODE 
from led.ledConstants import INCOMING_FRAME , SET_OVERLAY, SET_PASSIVE , PLAY_COMBO , HEARTBEAT


class LedLinkManager():

    #serial object
    def __init__(self , port , baudrate):
        self.ser = serial.Serial(timeout = 0)

        self.ser.port = port
        self.ser.baudrate = baudrate

        self._buf = b""
        self.droppedFrames=0

    def open(self):
        try:
            #bool types to set state of DTR and RTS line
            self.ser.rts = False
            self.ser.dtr = False

            if not OPEN_LED_SERIAL:
                print("[LEDLINKMANAGER] Port not Available")
                return False

            self.ser.open()


            result = self._request_check()

            if result == "OK":
                #connected
                print("[LEDLINKMANAGER] LED ESP CONNECTED")
            elif result == "WRONG":
                print("[LEDLINKMANAGER] WRONG ESP CONNECTED")
            elif result == "SILENT":
                print("[LEDLINKMANAGER] UNKNOWN ESP CONNECTED")


            return True
        
        except Exception as e:
            print(f"[LEDLINKMANAGER] Cant open serial port because of {e}")
            return False
        
    #close + destroy serial object
    def close(self):
        if self.is_connected():
            #connected, so close
            self.ser.close()
        else:
            #nothing connected
            print("[LEDLINKMANAGER] Closing ")


    def poll(self):
        #check
        if not self.is_connected():
            return [] #return frame 

        if not OPEN_LED_SERIAL:
            return []

        #read in waiting
        self._buf += self.ser.read(self.ser.in_waiting or 0)
        lines = self._buf.split(b"\n")
        self._buf = lines.pop()

        if len(self._buf)> 1024:
            self._buf = b""

        frames = []
        for line in lines:
            #parse throught incoming lines
            frame = self._parse(line)
            if frame is None:
                self.droppedFrames += 1
            else:
                frames.append(frame)

        return frames

    def send(self, prefix , *value):

        if not self.is_connected():
            return

        parts = [prefix]
        for v in value:
            parts.append(str(v))
        line = ",".join(parts) + "\n" #S,2,1\n
        
        self.ser.write(line.encode())

    def set_passive_animation(self, zone , pid):
        self.send(SET_PASSIVE,zone,pid)


    def set_overlay_animation(self , zone , oid):
        self.send(SET_OVERLAY,zone,oid)

    def send_heartbeat(self):
       self.send(HEARTBEAT)

    def read(self):
        pass

    def _parse(self , line): 
        try:
            frame = {}

            #decodes incominng lines from serial + removes spaces
            decoded = line.decode('utf-8').strip()
            #split gives back in indexes and removes commas
            parts = decoded.split(",")



            schema = INCOMING_FRAME.get(parts[0])

            if schema is None:
                return None
            
            if len(parts) -1 != len(schema):
                return None

            for name , value in zip(schema, parts[1:]):
                cast = schema[name]
                frame[name] = cast(value)

            #valid message - skip first element as its indentifier


            return (parts[0],frame)
        
        except Exception as e:
        
            print(f"[LEDLINKMANAGER] Parsing LED Error as {e}")
            return None

    #safety ping from correct ESP for correct ID
    def _request_check(self):
        #send request to ESP + timeout
        self.ser.write(b"?\n") #needs new byte line     

        clock = time.monotonic()

        TIMECHECK = 2

        deadline = clock + TIMECHECK

        while clock < deadline:
    
            #need to constantly poll 

            request = self.poll() #gets + parse

            for name , value in request:

                if name != "ID":
                    print(" [LEDLINKMANAGER] Not an ID frame ")
                    continue
                elif value["device"] == "LED":
                    print(" [LEDLINKMANAGER] ID frame + LED")
                    return "OK"
                else:
                    print(f"[LEDLINKMANAGER] EXPECTED LED , got {value['device']} ")
                    return "WRONG"

                
            clock = time.monotonic()
       
            time.sleep(0.1)

        return "SILENT"

    def is_connected(self):
        #theres a serial object
        return self.ser is not None and self.ser.is_open