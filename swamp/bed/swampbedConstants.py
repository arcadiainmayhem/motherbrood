from swamp.cicadaConstants import BROOD_IDS
from swamp.broodswarm import *

SWAMPBED_PARAMS_FRAME = {
    "calling_count": None ,
    "mean_arousal" : None
}

SWAMPBED_PARAMS_SETTINGS = {
    "calling_count" :  { "low" : 0 , "high" : len(BROOD_IDS) , "rise" : 1 , "fall" : 1} ,
    "mean_arousal" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},

}
#swampbed constants


BED_PREFIX = "/bed/"


BED_OSC_PORT = 9000

BED_RETURN_PORT = 9001

STATUS_PORT = 8000 #Flask

