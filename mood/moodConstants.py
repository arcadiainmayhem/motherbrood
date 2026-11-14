
from enum import Enum , IntEnum
from led.ledConstants import PassiveId, OverlayId , ZONECOUNT , ZoneId



class Mood(IntEnum):
    PASSIVE = 0,
    PLACATED = 1,
    OBSERVANT = 2,
    WARY = 3,
    FURIOUS = 4,
    EXCITED = 5,
    GACHA = 6,
    MATERNAL = 7,
    PREACHY = 8

STARTINGMOTHERMOOD = Mood.OBSERVANT

#TUNING
MIN_DWELL = 30
IDLE_TIME = 15
TOUCH_EXPIRY = 60

#mood -> led , sound , interaction
#params for mood changes
MOODRULES = {
    
}
MOTHERMOODS = {

  "IDLE" : {    
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
  "PLACATED" : {
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
  "WARY" : {
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
  "OBSERVANT" : {
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
  "FURIOUS" : {
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
  
  "EXCITED" : {
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
    
  "MATERNAL" : {
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
    
  "PREACHY" : {
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
   
  "GACHA" : {
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


