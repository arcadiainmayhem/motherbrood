from swamp.puredataManager import PuredataManager
from swamp.swampbedConstants import BED_OSC_PORT
from swamp.patches.patchlibrary import TEST_PATCH
from swamp.buglinkManager import BugLinkManager
from swamp.broodswarm import Broodswarm
from swamp.cicadaConstants import BROOD_IDS
from hardware.hardwareConstants import MOTHER_PORT,MOTHER_BAUD
import time





def main():
    puredatabed = PuredataManager(TEST_PATCH , BED_OSC_PORT)
    if not puredatabed.start():
        print("[MAIN] Puredatabed failed to start")

        return

    print("[MAIN] Swampbed Initialised")

    buglink = BugLinkManager( MOTHER_PORT , MOTHER_BAUD)

    buglink.open()

    print("[MAIN] Mother Port Open - Talking")

    swarm = Broodswarm(BROOD_IDS)

    try:
        while True:
            

            while (buglink.is_connected):
                time.sleep(0.1)

                frames = buglink.poll()


                if not frames:
                    continue


                for frame in frames:
                    now = time.monotonic()
                    swarm.update(frame , now)
                    
                    print("Cicadas: " , swarm.broodlings)



                puredatabed.send("/bed/openness" , frame["arousal"])
    

    except KeyboardInterrupt:
        #stop
        pass
    finally:
        puredatabed.stop()
        print("Swamp Stopped")

if __name__ == "__main__":
    main()