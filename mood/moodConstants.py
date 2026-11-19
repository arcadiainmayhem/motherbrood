
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
MIN_DWELL = 20
IDLE_TIME = 15
TOUCH_EXPIRY = 60
GESTURE_EXPIRY = 35
DECAY_VALUE = 0.02
JITTER = 0.08 #change later?

class GESTURES(Enum):
    SOOTHE = 1
    PROVOKE = 2
    OFFERING = 3
    WITHHOLD = 4
    PRAISE = 5
    SCOLD = 6
    POKE = 7
    WORSHIP = 8
    SPEAK = 9 
    DIVINE = 10

#mood -> led  sound , interaction
#params for mood changes
MOODRULES = {
    
}

TOUCH_EFFECTS= {
    "ZONE_EFFECT_1" : {
        "peace": 0.3,
        "irritability": -0.2,
        "affection": 0.4,
        "awareness": -0.1,    
    },
    "ZONE_EFFECT_2" : {
        "peace": -0.2,
        "irritability": 0.2,
        "affection": -0.3,
        "awareness": 0.3,   
    },
    "ZONE_EFFECT_3" : {
        "energy": -0.2,
        "affection": 0.4,
        "awareness": -0.1,   
    },
    "ZONE_EFFECT_4" : {
        "peace": -0.2,
        "irritability": 0.25,
        "energy": 0.4,
    },


}
MOTHERMOODS = {

  MOOD.IDLE : {    
      "led" : {
          #zone - animation
          "passive" : 
              PassiveId.PASSIVE_CALM, 
          
          "overlay" : 
              OverlayId.OVERLAY_TOUCHFLASH
          
      },
      "sound":{
          
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

  },         
}   


