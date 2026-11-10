
from enum import Enum , IntEnum

#MUST MATCH ESP SIDE - MENU OF LED EFFECTS
class PassiveId(IntEnum):
    SLOW_MAGENTA = 0
    SLOW_GREEN = 1
    SLOW_PULSE_YELLOW = 2


class OverlayId(IntEnum):
   FLASH = 0
   FLASHFADE = 1   
   FLASHDISPERSE = 2

STARTINGMOTHERMOOD = "IDLE"

#TUNING
MIN_DWELL = 30
IDLE_TIME = 15
TOUCH_EXPIRY = 60

ZONECOUNT = 8

#mood -> led , sound , interaction
#params for mood changes
MOODRULES = {
   "IDLE" : {
    "min_activity" : 0,
    "max_dwell_time" : 0,
    "max_idle_time" : 0,
    "max_touch_count" : 0,
   },
   "PLACATED" : {
      
  },
  "WARY" : {
        
  },
  "OBSERVANT" : {
        
  },
  "FURIOUS" : {
        
  },
  "EXCITED" : {
          
    },
  "MATERNAL" : {
          
    },
  "PREACHY" : {
          
    },
  "GACHA" : {
          
    },
}
MOTHERMOODS = {

  "IDLE" : {    
      "led" : {
          #zone - animation
          "passive" : {
              0 : PassiveId.SLOW_MAGENTA , 
              1: PassiveId.SLOW_MAGENTA , 
              2 : PassiveId.SLOW_MAGENTA,
          },
          "overlay" : {
              0 : OverlayId.FLASH,
              1: OverlayId.FLASH,
              2 : OverlayId.FLASH,
          },
      },
      "sound":{
          
      },
      "interaction" : {
          
      },
  },
  "PLACATED" : {
      "led" : {
          "passive" : {
              0 : PassiveId.SLOW_PULSE_YELLOW , 
              1: PassiveId.SLOW_PULSE_YELLOW , 
              2 : PassiveId.SLOW_PULSE_YELLOW,
          },
          "overlay" : {
              0 : OverlayId.FLASH,
              1: OverlayId.FLASH,
              2 : OverlayId.FLASH,
          },
      },
      "sound":{
          
      },
      "interaction" : {
          
      },      
  },
  "WARY" : {
        
  },
  "OBSERVANT" : {
        
  },
  "FURIOUS" : {
        
  },
  "EXCITED" : {
          
    },
  "MATERNAL" : {
          
    },
  "PREACHY" : {
          
    },
  "GACHA" : {
          
    },
} 

