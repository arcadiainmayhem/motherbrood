
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

STARTINGMOTHERMOOD = MOOD.IDLE

BASELINE = {
    "peace" : 0.45,
    "irritability" : 0.0,
    "awareness" : 0.0,
    "affection" : 0.0,
    "energy" : 0.0,
}

#TUNING
MIN_DWELL = 20
IDLE_TIME = 15
TOUCH_EXPIRY = 60
GESTURE_EXPIRY = 35
DECAY_VALUE = 0.01
JITTER = 0.02 #change later?

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

MOODPARAMS = {
    "min_peace",
    "max_peace",
    "min_irritability",
    "max_irritability",
    "min_affection",
    "max_affection",
    "min_awareness",
    "max_awareness",
    "min_energy",
    "max_energy",
}

#mood -> led  sound , interaction
#params for mood changes
MOOD_RULES = {
    MOOD.FURIOUS:   {"min_irritability": 0.7, "max_peace": 0.3},
    MOOD.WARY:      {"min_irritability": 0.4, "min_awareness": 0.3},
    MOOD.EXCITED:   {"min_energy": 0.6, "max_irritability": 0.4},
    MOOD.MATERNAL:  {"min_affection": 0.6, "min_peace": 0.4},   # 0.6 peace was hard to reach alongside 0.6 affection
    MOOD.PREACHY:   {"min_awareness": 0.6, "max_affection": 0.3},
    MOOD.PLACATED:  {"min_peace": 0.4, "max_irritability": 0.3},
    MOOD.OBSERVANT: {"min_awareness": 0.25},
}

TOUCH_EFFECTS= {
    "ZONE_EFFECT_1" : { "peace": 0.09, "irritability": -0.05,"affection": 0.08, "awareness": -0.05, },
    "ZONE_EFFECT_2" : { "peace": -0.08, "irritability": 0.1, "affection": -0.09, "awareness": 0.07,  },
    "ZONE_EFFECT_3" : { "energy": -0.12, "affection": 0.11, "awareness": -0.1,  },
    "ZONE_EFFECT_4" : { "peace": -0.12, "irritability": 0.13, "energy": 0.14, },
}

GESTURE_EFFECTS = {
    GESTURES.SOOTHE:   {"peace": 0.25, "irritability": -0.2, "energy": -0.1},          # calms     → PLACATED
    GESTURES.PROVOKE:  {"irritability": 0.25, "peace": -0.2, "energy": 0.15, "awareness": 0.1},  # → WARY/FURIOUS
    GESTURES.OFFERING: {"affection": 0.25, "energy": 0.15, "peace": 0.1},              # gift      → MATERNAL/EXCITED
    GESTURES.WITHHOLD: {"affection": -0.2, "irritability": 0.15, "awareness": 0.15},   # denied    → suspicious
    GESTURES.PRAISE:   {"energy": 0.2, "affection": 0.15, "peace": 0.1},               # flattered → EXCITED
    GESTURES.SCOLD:    {"irritability": 0.2, "affection": -0.15, "awareness": 0.2},    # told off  → WARY/PREACHY
    GESTURES.POKE:     {"awareness": 0.2, "irritability": 0.1, "energy": 0.1},         # grabs attention
    GESTURES.WORSHIP:  {"peace": 0.2, "affection": 0.2, "awareness": 0.15},            # event later
    GESTURES.SPEAK:    {"awareness": 0.25, "energy": 0.05},                            # she listens → OBSERVANT/PREACHY
    GESTURES.DIVINE:   {"awareness": 0.3, "energy": 0.2},                              # event later
}

#sound to PD? like events
MOTHERMOODS = {

  MOOD.IDLE : {    
      "led" : { "passive" : PassiveId.PASSIVE_CALM,  "overlay" : OverlayId.OVERLAY_TOUCHFLASH},
      "sound":{  },
  },
  MOOD.PLACATED : {
      "led" : {"passive" : PassiveId.PASSIVE_CALM, "overlay" :  OverlayId.OVERLAY_BLOOM,},
      "sound":{    },
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


