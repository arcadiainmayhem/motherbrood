

from core.utilities import scale,smoothing,deadband , clamp 
from gesture.gestureReader import GestureReader
from panel.panelConstants import *

class PanelDirector():
    
    def __init__(self, motherPanel, pureDataManager , moodDirector , gestureReader ):


        self.motherPanel = motherPanel # passed in
        self.pureDataManager = pureDataManager # passed in
        self.moodDirector = moodDirector # passed in 
        self.gestureReader = gestureReader

        self.lastSentPotValues  = {}

        #setup pots - loop through pots + set value to params

    def update(self , now):

        #---for pots
        for name, params in POT_MASTERLIST.items():
            if params is None:
                continue

            if name not in self.motherPanel.potValues:
                continue

            raw = self.motherPanel.potValues[name]

            #scale it before sending
            value = scale(raw, params.input_min, params.input_max , params.output_min , params.output_max)

            clamped = clamp(value, params.output_min , params.output_max )

            #skip if it hasnt moved enough
            last = self.lastSentPotValues.get(name)

            if last is not None and abs(clamped - last) < POT_DEADBAND:
                continue

            self.lastSentPotValues[name] = clamped

            self._send_destination(params , clamped , now)


        #---for buttons
        changes = self.motherPanel.take_changes()

        
        for name , value in changes.items():

            params = BUTTON_MASTERLIST.get(name)

            if params is None:
                continue

            #keys only matter when pressed 
            if params.buttonType == BUTTON_TYPES.MOMENTARY and value != 1:
                continue


            self._send_destination(params , value , now)

    

                  
    def _send_destination(self , params, value , now):


        if params.destination == DESTINATION_PLACES.PUREDATA:
            self.pureDataManager.send_panel(params.target,value)
        elif params.destination == DESTINATION_PLACES.CICADAS:
            print(f"[PANELDIRECTOR] SENDING PARAMS + VALUES TO CICADAS {params.target} , {value:.3f}")
        elif params.destination == DESTINATION_PLACES.FOR_PI:
            print(f"[PANELDIRECTOR] SENDING PARAMS + VALUES TO PI {params.target} {value:.3f}")
        elif params.destination == DESTINATION_PLACES.MOOD:
            self.gestureReader.on_press(params.name , now)
            print(f"[PANELDIRECTOR] SENDING NAME TO GESTURE READER -> {params.name}")

