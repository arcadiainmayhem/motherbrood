
from enum import Enum , IntEnum
from led.ledConstants import PassiveId, OverlayId , ZONECOUNT , ZoneId



class MOOD(IntEnum):
    IDLE = 0
    PLACATED = 1
    OBSERVANT = 2
    WARY = 3
    FURIOUS = 4
    EXCITED = 5
    GACHA = 6
    MATERNAL = 7
    PREACHY = 8

STARTINGMOTHERMOOD = MOOD.OBSERVANT

#TUNING
MIN_DWELL = 30
IDLE_TIME = 15
TOUCH_EXPIRY = 60

class GESTURES(Enum):
    SOOTHE = 1
    PROVOKE = 2
    FEED = 3
    WITHHOLD = 4
    PRAISE = 5
    SCOLD = 6

#mood -> led  sound , interaction
#params for mood changes
MOODRULES = {
    
}
MOTHERMOODS = {

  MOOD.Idle : {    
      "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_CALM, 
          
          "overlay" : 
              OverlayId.OVERLAY_TOUCHFLASH
          
      },
      "sound":{
          
      },
      "interaction" : {
          
      },
  },
  MOOD.PLACATED : {
      "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_CALM, 
          
          "overlay" : 
              OverlayId.OVERLAY_BLOOM,
          
      },
      "sound":{
          
      },
      "interaction" : {
             
  }
  },
  MOOD.WARY : {
    "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_WATCHFUL, 
          
          "overlay" : 
              OverlayId.OVERLAY_TOUCHFLASH,
          
      },
      "sound":{
          
      },
      "interaction" : {
          
        
  }
  },
  MOOD.OBSERVANT : {
        "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_WATCHFUL, 
          
          "overlay" : 
              OverlayId.OVERLAY_BLOOM,
          
      },
      "sound":{
          
      },
      "interaction" : {
          
    }
  },
  MOOD.FURIOUS : {
      "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_AGITATED, 
          
          "overlay" :
              OverlayId.OVERLAY_TOUCHFLASH,
          
      },
      "sound":{
          
      },
      "interaction" : {
          
      },
    },        
  
  MOOD.EXCITED : {
       "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_ELATED, 
          
          "overlay" : 
              OverlayId.OVERLAY_SPARKLE,
          
      },
      "sound":{
          
      },
      "interaction" : {
          
      },
  },         
    
  MOOD.MATERNAL : {
      "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_NURTURING, 
          
          "overlay" : 
              OverlayId.OVERLAY_BLOOM,
          
      },
      "sound":{
          
      },
      "interaction" : {
          
      },
  },          
    
  MOOD.PREACHY : {
      "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_NURTURING, 
        
          "overlay" : 
              OverlayId.OVERLAY_TOUCHFLASH,
          
      },
      "sound":{
          
      },
      "interaction" : {
          
      },
  },          
   
  MOOD.GACHA : {
       "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_ELATED, 
          
          "overlay" : 
              OverlayId.OVERLAY_SPARKLE,
          
      },
      "sound":{
          
      },
      "interaction" : {
          
      },
  },         
}   


