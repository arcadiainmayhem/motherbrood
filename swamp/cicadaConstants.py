

#SCHEMA OF CICADA - MUST MATCH WITH MOTHER
BUG_FRAME = {
    "type":int,
    "id" : int,
    "firmware":int,
    "uptime":int,
    "packetCount":int,

    "arousal" : float,
    "state" : int,
    "personality":int,
    
    "callingTimer" : float,
    #"seq" : int
}


#NUMBER OF CICADAS
BROOD_IDS = { 0  , 1 , 2 , 3, 4, 5, 6, 7, 8, 9}




#CICADA VARIABLES
BROOD_TIMEOUT = 5