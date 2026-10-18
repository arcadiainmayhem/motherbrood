
from enum import Enum
from dataclasses import dataclass

class DESTINATION_PLACES(Enum):
    PUREDATA = 1
    CICADAS = 2
    FOR_Pi = 3


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
    target:str
    buttonType: BUTTON_TYPES    

POT_DEADBAND = 0.005

POT_MASTERLIST = {

    "pot1" : PotParams("level_test", DESTINATION_PLACES.PUREDATA, "/panel/level"),
    "pot2" : PotParams("tone_test", DESTINATION_PLACES.PUREDATA, "/panel/tone"),
    "pot3" : None,
    "pot4" : None,
    "pot5" : None,
    "pot6" : None,

}


BUTTON_MASTERLIST = {
    "btn1" : ButtonParams("hush_test" , DESTINATION_PLACES.PUREDATA, "/panel/hush" , BUTTON_TYPES.MOMENTARY),
    "btn2" : None,
    "btn3" : None,
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

    # #group



    #zone
}