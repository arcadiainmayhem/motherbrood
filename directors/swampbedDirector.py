
from swamp.puredataManager import PuredataManager
from swamp.swampbedConstants import BED_OSC_PORT
from swamp.patches.patchlibrary import TEST_PATCH

from swamp.buglinkManager import BugLinkManager
from swamp.panellinkManager import PanellinkManager

from swamp.broodswarm import Broodswarm
from swamp.cicadaConstants import BROOD_IDS

from hardware.hardwareConstants import MOTHER_PORT,MOTHER_BAUD , MOTHER_PANEL_PORT

from core.utilities import scale , deadband , clamp
import time


class SwampbedDirector():


    def __init__(self):

      
        #swampbed variables
        #main switch to be on
        self.isSwampActive = False
        #check for audio connectivity
        self.isAudioConnected = False
        self.isAudioActive = False

        #check for patch availability


        #check connections


        #setup puredatamanager
        self.puredatabed = PuredataManager(TEST_PATCH , BED_OSC_PORT)
        #setup buglink to mother 
        self.buglink = BugLinkManager( MOTHER_PORT , MOTHER_BAUD)
        #setup panellink 
        self.panellink = PanellinkManager(MOTHER_PANEL_PORT, MOTHER_BAUD)


    #start PD , open port
    def start(self):
        #start puredata 
       

        if not self.puredatabed.start():
            print("[SWAMPBEDDIRECTOR] Puredata Not Started")
            return


        #start MOTHER PORT link
    

        if not self.buglink.open():
            print("[SWAMPBEDDIRECTOR] MOTHER Port Not Open")
            return

    
        if not self.panellink.open():
            print("[SWAMPBEDDIRECTOR] MOTHER Panel Port Not Open")
            return     
           
        #initialise swarm
        self.swarm = Broodswarm(BROOD_IDS)


        #after everything has been iniitialised
        self.isSwampActive = True
    
    #reads incoming frames
    def _read(self):
        try:
            if (self.buglink.is_connected()):
                time.sleep(0.1)
                
                frames = self.buglink.poll()

                if not frames:
                    return 

                print(f"[SWAMPBEDDIRECTOR] Frames: ",frames, ".There are ",self.buglink.droppedFrames, " Dropped Frames: ")       


                #map to cicada
                for frame in frames:

                    now = time.monotonic()

                    self.swarm.update(frame , now) 

                    print(f"[SWAMPBEDDIRECTOR] Cicadas :" , self.swarm.broodlings)



                                  
        except Exception as e:
            print(f"[SWAMPBEDDIRECTOR Cant read incoming frames because of : {e}] ")
    
    #main logic of what incoming data means
    def _decide(self):
        pass

    #send out commands . values to mothers 
    def send(self):

        print("[SWAMPBEDDIRECTOR] SENDING VALUE")

    def stop(self):
        #stop puredata
        self.puredatabed.stop()

        #close bug and panel link
        self.buglink.close()
        self.panellink.close()

    def restart(self):
        self.stop()
        self.start()

  


