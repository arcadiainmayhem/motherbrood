
from swamp.buglinkManager import BugLinkManager
from swamp.broodswarm import Broodswarm
from swamp.cicadaConstants import BROOD_IDS
from hardware.hardwareConstants import MOTHER_PORT,MOTHER_BAUD
import time
from swamp.cicadaConstants import BUG_FRAME


buglink = BugLinkManager( MOTHER_PORT, MOTHER_BAUD) 


#open
buglink.open()
print("[SWAMPBED] MOTHER ESP LINKED TO MOTHERPI VIA SERIAL")
print(list(BUG_FRAME))

swarm = Broodswarm(BROOD_IDS)

try: 
#incoming messages
#while the port is open

    while (buglink.is_connected()):
        time.sleep(0.1)

        frames = buglink.poll()
        print("[TEST] Frames Polled")
        #check against empty
        if not frames:
            continue

        print("[TEST]: ", frames)    
            
        for frame in frames:

            now = time.monotonic()

            swarm.update(frame,now)



            print("Cicadas: " , swarm.broodlings)


except KeyboardInterrupt:
    buglink.close()
    print(f"[TEST] Stopping ")