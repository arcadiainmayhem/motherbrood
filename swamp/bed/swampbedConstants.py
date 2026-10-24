from swamp.cicada.cicadaConstants import BROOD_IDS



# SWAMPBED_PARAMS_FRAME = {   
#     #continous
#     # "calling_count": None ,
#     # "mean_arousal" : None,

#     "density" : None,
#     "tension" : None,
#     "rest" : None,
#     "unrest" : None,
#     #event
#     "call_onset" : None,
#     "swarm_density" : None,
# }


BED_CONTINUOUS = {
    # "calling_count" :  { "low" : 0 , "high" : len(BROOD_IDS) , "rise" : 1 , "fall" : 1} ,
    # "mean_arousal" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},  

    "density" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
    "tension" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
    "rest" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
    "unrest" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
}

BED_EVENTS = ["call_onset" , "swarm_density"]

        #event
#     "call_onset" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
#     "swarm_density" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
# }



# SWAMPBED_PARAMS_SETTINGS = {
#     # "calling_count" :  { "low" : 0 , "high" : len(BROOD_IDS) , "rise" : 1 , "fall" : 1} ,
#     # "mean_arousal" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},  

#     "density" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
#     "tension" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
#     "rest" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
#     "unrest" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},

#         #event
#     "call_onset" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
#     "swarm_density" : {  "low" : 0.0 , "high" : 1.0 , "rise" : 0.5 , "fall" : 0.1},
# }
#swampbed constants


BED_PREFIX = "/bed/"
PANEL_PREFIX = "/panel/"

BED_OSC_PORT = 9000
PANEL_OSC_PORT = 9001

STATUS_PORT = 8000 #Flask

