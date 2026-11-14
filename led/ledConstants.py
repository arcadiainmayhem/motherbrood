from enum import Enum , IntEnum

#MIRRORS config.h + LEDPresets.h - CHANGE BOTH

class ZoneId(IntEnum):
  ZONE_A = 0,
  ZONE_B = 1,
  ZONE_C = 2,
  ZONE_D = 3,
  ZONE_E = 4,
  ZONE_F = 5,
  ZONE_G = 6,
  ZONE_H = 7,

ZONECOUNT = len(ZoneId)

class PassiveId(IntEnum):
  PASSIVE_CALM = 0,
  PASSIVE_ALERT = 1,
  PASSIVE_AGITATED = 2,
  PASSIVE_WATCHFUL = 3,
  PASSIVE_ELATED = 4,
  PASSIVE_NURTURING = 5,


class OverlayId(IntEnum):
  OVERLAY_TOUCHFLASH = 0,
  OVERLAY_BLOOM = 1,
  OVERLAY_SPARKLE = 2,


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