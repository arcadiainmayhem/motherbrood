from panel.panelConstants import POT_MASTERLIST , BUTTON_MASTERLIST





class MotherPanel():
    
    def __init__(self):
        #container for incoming
        self.potValues = {}
        self.buttonValues = {}

        self.panelPeripheryValues={}

        
        self.buttonStatus = {}

        #storage

        self.pendingValues = {}
        
        #empty previous button values first frame?  
        self.previousButtonValues = {}


    def update(self, frame ):

        self.previousButtonValues = self.buttonValues.copy()

        #check incoming frame
        
        #store pot values from incoming frame
        for name in POT_MASTERLIST:
            self.potValues[name] = frame[name]
        #store button values
        for name in BUTTON_MASTERLIST:
            self.buttonValues[name] = frame[name]  
        #store packet count 
        self.panelPeripheryValues["packetCount"] = frame["packetCount"]




    #1 is pressed. 0 is no activity


    def button_changes(self):
        #decide if something happened
        #current - in order
        #clear every round
        self.buttonStatus = {}
        #for momentary buttons
        for name , value in self.buttonValues.items():
            #guard against empty
            if name not in self.previousButtonValues:
                continue
            #check difference in value        
            previousValue = self.previousButtonValues[name]

            outcome = value - previousValue
                #difference - change - pressed
            if outcome == -1 :
                #print("[MOTHERPANEL] No Press")  

                #for latching buttons 
                pass 
            elif outcome == 1:

                print("[MOTHERPANEL] Pressed")  

                self.buttonStatus[name] = value


        return self.buttonStatus



