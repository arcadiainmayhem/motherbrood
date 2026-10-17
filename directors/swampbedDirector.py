
from swamp.puredataManager import PuredataManager
from swamp.buglinkManager import BugLinkManager
from swamp.panellinkManager import PanellinkManager
from panel.motherpanel import MotherPanel
from directors.panelDirector import PanelDirector

from swamp.bed.swampbedConstants import BED_OSC_PORT
from swamp.patches.patchlibrary import TEST_PATCH


from swamp.broodswarm import Broodswarm
from swamp.bed.bedmapper import Bedmapper

from swamp.cicadaConstants import BROOD_IDS

from swamp.bed.swampbedConstants import SWAMPBED_PARAMS_SETTINGS , BED_PREFIX , PANEL_PREFIX

from core.installationConstants import DEV_MODE
from hardware.hardwareConstants import MOTHER_PORT,MOTHER_BAUD , MOTHER_PANEL_PORT


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


        #setup motherpanel
        self.motherPanel = MotherPanel()
        #setup puredatamanager
        self.puredatabed = PuredataManager(TEST_PATCH , BED_OSC_PORT)
        #setup buglink to mother 
        self.buglink = BugLinkManager( MOTHER_PORT , MOTHER_BAUD)
        #setup panellink 
        self.panellink = PanellinkManager(MOTHER_PANEL_PORT, MOTHER_BAUD)
        #setup Bedmapper
        self.bedmapper = Bedmapper()

        #setup motherpanel director
        self.panelDirector = PanelDirector(self.motherPanel , self.puredatabed)

        #initialise swarm
        self.swarm = Broodswarm(BROOD_IDS)

    #start PD , open port
    def start(self):
        #start puredata 

        if DEV_MODE:
            print ("[SWAMPBEDDIRECTOR] Starting in DEVMODE")
            return True
        
        else:
            if not self.puredatabed.start():
                print("[SWAMPBEDDIRECTOR] Puredata Not Started")
                return False


            #start MOTHER PORT link
            if not self.buglink.open():
                print("[SWAMPBEDDIRECTOR] MOTHER Port Not Open")
                return False

        
            if not self.panellink.open():
                print("[SWAMPBEDDIRECTOR] MOTHER Panel Port Not Open")
                return False      


            #after everything has been iniitialised
            self.isSwampActive = True
            print("[SWAMPBEDDIRECTOR] PUREDATA , MOTHER PORT , PANEL PORT - Everything Started Successfully")

            return True
    
    def tick(self, now):
        time.sleep(0.1)

        self._read_bugframes(now)
        self._read_panelframes(now)
        self._decide(now)
        self._send()

    #reads incoming frames
    def _read_bugframes(self, now):
        try:

            frames = self.buglink.poll()
     

            #print(f"[SWAMPBEDDIRECTOR] Frames: ",frames, ".There are ",self.buglink.droppedFrames, " Dropped Frames: ")       


            #map to cicada
            for frame in frames:

                self.swarm.update(frame , now) 

                bugId = frame['id']            

                #print(f"[SWAMPBEDDIRECTOR] Current Updated Cicada: BUGID : {bugId} - {self.swarm.broodlings[bugId]}")

                
                print(f"[SWAMPBEDDIRECTOR] Current Cicadas: BUGID : {bugId} - {self.swarm.broodlings}")

        except Exception as e:
            print(f"[SWAMPBEDDIRECTOR Cant read incoming frames because of : {e}] ")

    def _read_panelframes(self,now):
        try:
            panel_frames = self.panellink.poll()


            for frame in panel_frames:
                self.motherPanel.update(frame)
                self.panelDirector.update()


                print(f"[SWAMPBEDDIRECTOR] Current Pot + Button Reads: {frame}")


        except Exception as e:
            print(f"[SWAMPBEDDIRECTOR Cant read incoming frames because of : {e}] ")

    def _decide(self , now):

        #continuous mapping
        for_decision = {}

        for name in SWAMPBED_PARAMS_SETTINGS:
            method = getattr(self.swarm , name)
            for_decision[name] = method(now)



        #print(for_decision)
        print(f"[SWAMPBEDDIRECTOR] Calling Count now : {self.swarm.calling_count(now)}")
        
        #to updates
        self.bedmapper.update(for_decision)
 

        #events 

        #print("[SWAMPBEDDIRECTOR] DECIDING WHAT TO DO WITH VALUE")

    #send out commands . values to mothers 
    def _send(self):
        #send for bed mapper

        for name,value in self.bedmapper.bedvalues.items():
            self.puredatabed.send(f"{BED_PREFIX}{name}" , value)



        #send for panels - pots        
        for name,value in self.motherPanel.potValues.items():
            self.puredatabed.send(f"{PANEL_PREFIX}{name}" , value)

            print(f"[SWAMPBEDDIRECTOR] SENDING ADDRESS: {name} , VALUE: {value}")

        #send for panels - butotns      
        for name, value in self.motherPanel.buttonValues.items():
            self.puredatabed.send(f"{PANEL_PREFIX}{name}" , value)

            print(f"[SWAMPBEDDIRECTOR] SENDING ADDRESS: {name} , VALUE: {value}")

    def stop(self):
        #stop puredata - [MIGHT NOT BE STOPPING IT PROPERLY]
        self.puredatabed.stop() 

        #close bug and panel link
        self.buglink.close()
        self.panellink.close()

    def restart(self):
        self.stop()
        self.start()

  


