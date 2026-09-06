from swamp.puredataManager import PuredataManager
from swamp.swampbedConstants import BED_OSC_PORT
from swamp.patches.patchlibrary import TEST_PATCH
from core.installationConstants import DEV_MODE , AUDIO_DEVICE 
from directors.swampbedDirector import SwampbedDirector
import time





def main():
    puredatabed = PuredataManager(TEST_PATCH , AUDIO_DEVICE , BED_OSC_PORT)
    if not puredatabed.start():
        print("[MAIN] Puredatabed failed ton start")

        return

    print("[MAIN] Swampbed Initialised")


    # swampbed = SwampbedDirector()
    # swampbed.start()


    try:
        while True:
            time.sleep(0.1)

            puredatabed.send("/swampbed/openess" , 0.8)
    

    except KeyboardInterrupt:
        #stop
        pass
    finally:
        puredatabed.stop()
        print("Swamp Stopped")

if __name__ == "__main__":
    main()