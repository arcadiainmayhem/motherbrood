
from mood.moodConstants import MOTHERMOODS , MOODRULES , MIN_DWELL , IDLE_TIME , TOUCH_EXPIRY , STARTINGMOTHERMOOD , MOOD , GESTURE_EXPIRY , TOUCH_EFFECTS , DECAY_VALUE , JITTER
from led.ledConstants import ZoneId
import time
import random
from core.utilities import clamp

class MoodDirector():

    #starting mood + ref to link manager
    def __init__(self , LedLinkManager):
        self.ledlink = LedLinkManager

        #initialises initial mood
        self.currentMood = STARTINGMOTHERMOOD

        self.moodStart = time.monotonic()
        #time

        self.lastTouchTime = None
        self.touchTimes = []
        self.touchLog = []

        self.gestureLog = []
        
        self.gestureTimestamp = []


        #track current zone?
        self.lastUpdate = None
        #track mentality
        self.state  = {
                "peace" : 0.05,
                "irritability" : 0.0,
                "awareness" : 0.0,
                "affection" : 0.05,
                "energy" : 0.0,
            }
    
        #health check for mood being present
        for mood in MOOD:
              if mood not in MOTHERMOODS:
                  print(f"[MOODDIRECTOR] Missing Mood : {mood}")
                  raise ValueError("MISSING MOOD")

  

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
   

        #reset
        kept = []
        for entry in self.gestureLog:
            t = entry[1]
            if now - t <= GESTURE_EXPIRY:
                kept.append(entry)
        self.gestureLog = kept

        
        self.fading_state_values(self.state,now)

    #checks mapping + telling led manager which zone to play
    def change_mood(self, mood ,  now ):

        print(f"[MOODIRECTOR] {self.currentMood} -> {mood}")

        self.currentMood = mood
        self.moodStart = now

        self._send_mood(mood)
 

    def reapply(self):
        self._send_mood(self.currentMood)

    def _send_mood(self, mood ):

        led = MOTHERMOODS[mood]["led"]

        for zone in ZoneId:


            pid = led["passive"]
            self.ledlink.set_passive_animation(zone, pid)
            oid = led["overlay"]
            self.ledlink.set_overlay_animation(zone, oid)
                            

    def _pick_mood(self,now):

  
        #if no touch yet, or too long no touch, change 
        if self.lastTouchTime is None or (now - self.lastTouchTime) >= IDLE_TIME:
            return MOOD.IDLE
        
        return MOOD.PLACATED
        #use rules to determine

    #called by swamp bed director , passes in chosen gesture ( post classify )
    def on_gesture(self, gesture , now):    


        self.gestureLog.append((gesture ,now))

        #when hit certain gesture , affect state params

        print(f"[MOODDIRECTOR] Chosen Gesture: {self.gestureLog}, TimeStamp: {now}")


    #records a touch + mood pressure
    def on_touch(self , zone , now):

        #check 

        self.lastTouchTime = now
        #counter 
        
        #append to a list
        self.touchTimes.append(now)
        #see what has been touched
        self.touchLog.append((zone,now))

        #apply effects to state - currently random effect 
        chosen = random.choice(list(TOUCH_EFFECTS.values()))
        for effect , value in chosen.items():
            if effect in self.state:
                jitterVal = random.uniform(-JITTER , JITTER)
                currentVal = self.state[effect] 
                outcome = currentVal+ ( value + jitterVal )
                clamped = clamp(outcome , 0.0 , 1.0)
                #return to dict
                self.state[effect] = clamped

        print(f"[MOODDIRECTOR] Current Zone being Touched:{zone} , Timestamp: {now}")

    def _apply_effects(self , effect):
        pass

    def fading_state_values(self, state , now):

        if self.lastUpdate is None:
            self.lastUpdate = now
            return
        
        lastFaded = self.lastUpdate[0]
        
        delta = now - lastFaded
        #update dictionary
        for x in state:
            value = state[x]
            #change to decay dict ( different decay values )
            step = DECAY_VALUE * delta
            faded = value - step
            final = clamp(faded, 0.0 , 1.0)
            state[x] = final

                
        self.lastUpdate = now