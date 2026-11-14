
from enum import Enum
from dataclasses import dataclass
from mood.moodConstants import GESTURES

PANEL_POT_COUNT = 6
PANEL_BUTTON_COUNT = 11

class DESTINATION_PLACES(Enum):
    PUREDATA = 1
    CICADAS = 2
    FOR_PI = 3
    MOOD = 4

class BUTTON_TYPES(Enum):
    MOMENTARY = 1
    LATCHING = 2


@dataclass(frozen=True)
class PotParams:
    meaning:str
    destination : DESTINATION_PLACES
    target:str
    input_min: int = 0
    input_max: int = 4095
    output_min: float = 0.0
    output_max: float = 1.0

@dataclass(frozen=True)
class ButtonParams:
    meaning:str
    destination : DESTINATION_PLACES
    gesture: GESTURES
    target:str
    buttonType: BUTTON_TYPES    

POT_DEADBAND = 0.005

POT_MASTERLIST = {

    "pot1" : PotParams("level_test", DESTINATION_PLACES.PUREDATA, "/panel/level"),
    "pot2" : PotParams("tone_test", DESTINATION_PLACES.PUREDATA, "/panel/tone"),
    "pot3" : PotParams("A", DESTINATION_PLACES.PUREDATA, "/panel/tone"),
    "pot4" : PotParams("B", DESTINATION_PLACES.PUREDATA, "/panel/tone"),
    "pot5" : PotParams("C", DESTINATION_PLACES.PUREDATA, "/panel/tone"),
    "pot6" : PotParams("D", DESTINATION_PLACES.PUREDATA, "/panel/tone"),

}


BUTTON_MASTERLIST = {
    "btn1" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE , "/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn2" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn3" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn4" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),

    "btn5" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn6" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn7" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn8" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),

    "btn9" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn10" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn11" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, GESTURES.SOOTHE ,"/panel/hush" , BUTTON_TYPES.MOMENTARY),

}    



PANEL_FRAME = {
    
    "packetCount":int,
    "firmware" : int,

    #pots - knobs
    "pot1" : int,
    "pot2" : int,
    "pot3" : int,
    "pot4" : int,
    "pot5" : int,
    "pot6" : int,
    
    #buttons - 0 or 1
    "btn1" : int,
    "btn2" : int,
    "btn3" : int,
    "btn4" : int,

    # #group



    #zone
}