from panel.panelConstants import POT_MASTERLIST , BUTTON_MASTERLIST , POT_ALPHA





class MotherPanel():
    
    def __init__(self):
        #container for incoming
        self.potValues = {}
        self.buttonValues = {}

        self.panelPeripheryValues={}

        #storage

        self.pendingButtonValues = {} #mailbox
        
        #empty previous button values first frame? 


    #1 is pressed. 0 is no activity
    def update(self, frame ):

        #self.previousButtonValues = self.buttonValues.copy()

        #check incoming frame
    
        
        #-- smooth once before storing
        for name in POT_MASTERLIST:
            raw = frame[name]
            #first time
            if name not in self.potValues:
                self.potValues[name] = raw
            else:
                old = self.potValues[name]
                self.potValues[name] = old + POT_ALPHA * (raw - old)
            
        #--compare with prev button
        for name in BUTTON_MASTERLIST:
    
            #old
        
            oldValue = self.buttonValues.get(name)

            newValue = frame[name]

            if oldValue != newValue:
                self.pendingButtonValues[name] = newValue

            self.buttonValues[name] = newValue
        
        #store packet count 
        self.panelPeripheryValues["packetCount"] = frame["packetCount"]
        

    def take_changes(self):
        changes = self.pendingButtonValues
        self.pendingButtonValues = {}
        return changes

