from swamp.bed.swampbedConstants import SWAMPBED_PARAMS_SETTINGS
from swamp.broodswarm import Broodswarm
from core.utilities import *


class Bedmapper:


    def __init__(self):

        self.bedvalues = {} 

        #storing container
        for name in SWAMPBED_PARAMS_SETTINGS:
            self.bedvalues[name] = 0.0

    def update(self , descriptors):
      
        #incoming values

        #name is the key , settings is the value ( dict )
        for name , settings in SWAMPBED_PARAMS_SETTINGS.items():




            #if name not in incoming descriptors
            if name not in descriptors:
                print(f"[BEDMAPPER] {name} Not in Incoming Message")
                continue

       

            #fresh values coming in
            amount = descriptors[name] 


            current_value = self.bedvalues[name]
            low = settings["low"]
            high = settings["high"]         
            rise = settings["rise"]
            fall = settings["fall"]       
            
            #scale
            scaled = scale(amount , low , high , 0 , 1 )
                
            #clamp
            clamped = clamp(scaled, 0 , 1)

            smoothed_value = smoothing(current_value , clamped , rise , fall )

            self.bedvalues[name] = smoothed_value

            print("smoothed_value: ", name , smoothed_value)
                


    