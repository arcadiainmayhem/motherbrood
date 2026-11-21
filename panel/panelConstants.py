
from enum import Enum
from dataclasses import dataclass
from mood.moodConstants import GESTURES

PANEL_POT_COUNT = 6
PANEL_BUTTON_COUNT = 11

class DESTINATION_PLACES(Enum):
    PUREDATA = 1
    CICADAS = 2
    FOR_PI = 3
    GESTURE = 4

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
    # meaning:str
    destination : DESTINATION_PLACES
    name : str
    buttonType: BUTTON_TYPES    

POT_DEADBAND = 0.005
POT_ALPHA = 0.25

POT_MASTERLIST = {
    "pot1": PotParams("openness",  DESTINATION_PLACES.PUREDATA, "/panel/openness"),
    "pot2": PotParams("darkness",  DESTINATION_PLACES.PUREDATA, "/panel/darkness",  output_min=0.1, output_max=0.9),
    "pot3": PotParams("resonance", DESTINATION_PLACES.PUREDATA, "/panel/resonance", output_max=0.85),
    "pot4": PotParams("mud",       DESTINATION_PLACES.PUREDATA, "/panel/mud",       output_max=0.7),
    "pot5": PotParams("space",     DESTINATION_PLACES.PUREDATA, "/panel/space",     output_min=0.1, output_max=0.8),
    "pot6": PotParams("level",     DESTINATION_PLACES.PUREDATA, "/panel/level",     output_min=0.2, output_max=0.9),
}


BUTTON_MASTERLIST = {
    "btn1" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),
    "btn2" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),
    "btn3" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),
    "btn4" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),

    "btn5" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),
    "btn6" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),
    "btn7" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),
    "btn8" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),

    "btn9" : ButtonParams( DESTINATION_PLACES.GESTURE ,  BUTTON_TYPES.MOMENTARY),
    "btn10" : ButtonParams( DESTINATION_PLACES.GESTURE , BUTTON_TYPES.MOMENTARY),
    "btn11" : ButtonParams( DESTINATION_PLACES.GESTURE , BUTTON_TYPES.MOMENTARY),

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
    "btn5" : int,
    "btn6" : int,
    "btn7" : int,
    "btn8" : int,
    "btn9" : int,
    "btn10" : int,
    "btn11" : int,


}