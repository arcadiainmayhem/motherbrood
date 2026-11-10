

LED_FRAME = {
    
    "zone": int,
    "state": int,
    "passiveId": int,
    "overlayId": int,
     
}

TOUCH_FRAME = {
    "zone" : int,
}

INCOMING_FRAME = {
    "ID" : {"device" : str},
    "T" : TOUCH_FRAME,
    
}

#OUTGOING FRAME
SET_PASSIVE = "S"
SET_OVERLAY = "O"
PLAY_COMBO  = "C"
HEARTBEAT   = "H"