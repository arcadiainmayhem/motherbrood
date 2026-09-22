from swamp.buglinkManager import BugLinkManager
from swamp.broodswarm import Broodswarm
from swamp.cicadaConstants import BROOD_IDS
import time



buglink = BugLinkManager("COM3", 115200)
swarm = Broodswarm(BROOD_IDS)



lines = [
 b"B,0,CALLING,0.83,1042",
 b"B,0,HATING,0.83,1042,.022",
 b"B,1,RISING,0.21,7",
 b"#booting",
 b"B,2,CALLING",
 b"garbage",
 b"B,0,CALLING,abc,1042",
 b"B,999,CALLING,0.83,1042",
 b""  
]


now = 100.0
for line in lines:
    parsed = buglink._parse(line)
    print(line, "-> " , parsed)

    #current time
    now += 1.0

    if parsed is None:
        continue

    swarm.update(parsed , now)


    print("Cicadas: ", swarm.broodlings)
