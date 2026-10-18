from panel.panelConstants import POT_MASTERLIST , BUTTON_MASTERLIST





class MotherPanel():
    
    def __init__(self):
        #container for incoming
        self.potValues = {}
        self.buttonValues = {}

        self.panelPeripheryValues={}

        self.previousButtonValues = {}
        #
        self.buttonStatus = {}

        #empty previous button values first frame?  
        self.previousButtonValues = {}


    def update(self, frame ):

        self.previousButtonValues = self.buttonValues.copy()

        #check incoming frame
        
        #store pot values
        for name in POT_MASTERLIST:
            self.potValues[name] = frame[name]
        #store button values
        for name in BUTTON_MASTERLIST:
            self.buttonValues[name] = frame[name]  
        #store packet count 
        self.panelPeripheryValues["packetCount"] = frame["packetCount"]

        

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



