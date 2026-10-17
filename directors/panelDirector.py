

from core.utilities import scale,smoothing,deadband , clamp
from panel.panelConstants import *

class PanelDirector():
    
    def __init__(self, motherPanel, pureDataManager):


        self.motherPanel = motherPanel
        self.pureDataManager = pureDataManager

        self.lastSentPotValues  = {}

        #setup pots - loop through pots + set value to params

    def update(self):

        #for pots
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

            self._send_destination(params , clamped)


        #for buttons
        self.motherPanel.button_changes()

    def _send_destination(self , params, value):
        if params.destination == DESTINATION_PLACES.PUREDATA:
            self.pureDataManager.send(params.target,value)
        elif params.destination == DESTINATION_PLACES.CICADAS:
            print(f"[PANELDIRECTOR] SENDING PARAMS + VALUES TO CICADAS {params.target} , {value:.3f}")
        elif params.destination == DESTINATION_PLACES.FOR_PI:
            print(f"[PANELDIRECTOR] SENDING PARAMS + VALUES TO PI {params.target} {value:.3f}")
        

