
from mood.moodConstants import MOTHERMOODS , MOODRULES , MIN_DWELL , IDLE_TIME , TOUCH_EXPIRY , STARTINGMOTHERMOOD , Mood
from led.ledConstants import ZoneId
import time

class MoodDirector():

    #starting mood + ref to link manager
    def __init__(self , LedLinkManager):
        self.ledlink = LedLinkManager



        #initialises initial mood
        self.currentMood = STARTINGMOTHERMOOD

        self.moodStart = time.monotonic()
        #time

        self.lastTouchTime = None
        
        #track current zone?

  

        self.touchTimes = []
        

    #reads touch events , checks combo + decides whether mood should change
    def update(self, now):
        

        #check using poll 
        frame = self.ledlink.poll()

        #check for touch frame
        for kind, data in frame:
            #touch event

            if kind == "T":
             self.on_touch(data["zone"], now)

        #decide target 
        target = self._pick_mood(now) #gets string for mood

        #if target mood isnt current mood, and time has passed minimum dwell
        if target != self.currentMood and (now - self.moodStart) >= MIN_DWELL:
            self.change_mood(target , now)

        #reset
        self.touchTimes = [t for t in self.touchTimes if now - t <= TOUCH_EXPIRY]


    
    #checks mapping + telling led manager which zone to play
    def change_mood(self, mood ,  now ):

        print(f"[MOODIRECTOR] {self.currentMood} -> {mood}")

        self.currentMood = mood
        self.moodStart = now

        self._send_mood(mood)
 

    def reapply(self):
        self._send_mood(self.currentMood)

    def _send_mood(self, mood ):
        
        for zone in ZoneId:
            led = MOTHERMOODS[mood]["led"]

        pid = led["passive"]
        self.ledlink.set_passive_animation(zone, pid)
        oid = led["overlay"]
        self.ledlink.set_overlay_animation(zone, oid)
                        

    def _pick_mood(self,now):
        #if no touch yet, or too long no touch, change 
        if self.lastTouchTime is None or (now - self.lastTouchTime) >= IDLE_TIME:
            return Mood.PASSIVE
        
        return Mood.PLACATED
        #use rules to determine


    #records a touch + mood pressure
    def on_touch(self , zone, now):

        #check 

        self.lastTouchTime = now
        #counter 
        
        #append to a list
        self.touchTimes.append(now)
