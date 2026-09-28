from swamp.puredataManager import PuredataManager
from swamp.swampbedConstants import BED_OSC_PORT
from swamp.patches.patchlibrary import TEST_PATCH
from swamp.buglinkManager import BugLinkManager
from swamp.broodswarm import Broodswarm
from swamp.cicadaConstants import BROOD_IDS

from hardware.hardwareConstants import MOTHER_PORT,MOTHER_BAUD
import time


from directors.swampbedDirector import SwampbedDirector

def main():

    #start
    swampbed = SwampbedDirector()
    swampbed.start()

    print("[MAIN] Swampbed Started Successfully ")

    try:         
        while True:
            time.sleep(0.1)
            
            swampbed.send()           


    except KeyboardInterrupt:
        #stop
        pass

    finally:
        swampbed.stop()
        print("[MAIN] Swamp Stopped")

if __name__ == "__main__":
    main()