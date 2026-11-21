
from mood.moodConstants import MOTHERMOODS , MOOD_RULES , MIN_DWELL , TOUCH_EXPIRY , STARTINGMOTHERMOOD , MOOD , GESTURES, MOODPARAMS, BASELINE, GESTURE_EXPIRY , TOUCH_EFFECTS , DECAY_VALUE , JITTER , GESTURE_EFFECTS
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

        self.currentZoneTouched  = None
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
                "peace" : 0.0,
                "irritability" : 0.0,
                "awareness" : 0.0,
                "affection" : 0.0,
                "energy" : 0.0,
            }   

        self.health_check()
    

  

    #reads touch events , checks combo + decides whether mood should change
    def update(self, now):

        
        #check using poll 
        frame = self.ledlink.poll()

        #check for touch frame
        for kind, data in frame:
            #touch event

            if kind == "T":
             self.on_touch(data["zone"], now)

        #decide mood 
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

        print(f"[MOODDIRECTOR] Curren State { self.state }")

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
                            

    def _rule_matches(self, rule , incoming ):


        #minimums
        for drive in incoming:
            check = f"min_{drive}"
            if check in rule:
                if incoming[drive] < rule[check]:     
                    return False
        #maximum        
            check = f"max_{drive}"
            if check in rule:
                if incoming[drive] > rule[check]: 
                    return False       
        
        return True
    
    def _pick_mood(self,now):
        #use rules to determine

        #check current state
        incoming = self.state

        for mood , rule in MOOD_RULES.items():
            if self._rule_matches(rule , incoming):
                return mood

        return MOOD.IDLE
  

    def _apply_effects(self , chosen):
        #apply effects to state - currently random effect 

        for effect , value in chosen.items():
            if effect in self.state:
                jitterValue = random.uniform(-JITTER , JITTER)
                currentVal = self.state[effect]
                outcome = currentVal + (value + jitterValue)
                clamped = clamp(outcome , 0.0 , 1.0)
                #return to dict
                self.state[effect] = clamped

        print(f"[MOODDIRECTOR] Current Effect being Applied :{chosen} ")

    #called by swamp bed director , passes in chosen gesture ( post classify )
    def on_gesture(self, gesture , now):    


        self.gestureLog.append((gesture ,now))

        chosen = GESTURE_EFFECTS[gesture]
        #when hit certain gesture , affect state params

        self._apply_effects(chosen)

        print(f"[MOODDIRECTOR] Chosen Gesture : {gesture}, Previous Gestures: {self.gestureLog}, TimeStamp: {now}")



    #records a touch + mood pressure
    def on_touch(self , zone , now):

        #check 

        self.lastTouchTime = now
        #counter 
        
        #append to a list
        self.touchTimes.append(now)
        #see what has been touched
        self.touchLog.append((zone,now))

        self.currentZoneTouched = zone

        #apply effects to state - currently random effect 
        chosen = random.choice(list(TOUCH_EFFECTS.values()))

        self._apply_effects(chosen)


        print(f"[MOODDIRECTOR] Current Zone being Touched:{zone} , Timestamp: {now}")

    def get_current_zone_touched(self):
        return self.currentZoneTouched 

    def _on_mood_change(self , mood):
        #send to pd
        pass

    def get_current_mood(self):
        return self.currentMood

    def fading_state_values(self, state , now):

        if self.lastUpdate is None:
            self.lastUpdate = now
            return
        
        lastFaded = self.lastUpdate
        
        delta = now - lastFaded
        #update dictionary
        for x in state:
                value = state[x]
                #change to decay dict ( different decay values )
                step = DECAY_VALUE * delta

                if value != BASELINE[x]:
                    baseline = BASELINE[x] 

                    if value > baseline:
                        final = clamp(value - step, baseline, 1.0)
                    elif value < baseline:
                        final = clamp(value + step, 0.0 , baseline)
                        
                        
                self.state[x] = final
                
        self.lastUpdate = now


    def health_check(self):
        #health check for mood being present
        for mood in MOOD:
              if mood not in MOTHERMOODS:
                print(f"[MOODDIRECTOR] Missing Mood : {mood}")
                raise ValueError("MISSING MOOD")

        for rule in MOOD_RULES.values():
                for param in rule:
                    if param not in MOODPARAMS:
                        print(f"[MOODDIRECTOR] Missing Mood Rule : {param}")
                        raise ValueError("MISSING RULE")

        for gesture in GESTURES:
            if gesture not in GESTURE_EFFECTS:
                print(f"[MOODDIRECTOR] Missing Gesture : {gesture}")
                raise ValueError("MISSING GESTURE")

        for drive in TOUCH_EFFECTS.values():
            for param in drive:
                if param not in self.state:
                    print(f"[MOODDIRECTOR] Missing Param in Touch Effects : {param}")
                    raise ValueError("MISSING DRIVE IN TOUCH EFFECTS")                      
            
        for drive in GESTURE_EFFECTS.values():
            for param in drive:
                if param not in self.state:
                    print(f"[MOODDIRECTOR] Missing Drive in Gesture Effects : {param}")
                    raise ValueError("MISSING DRIVE IN GESTURE EFFECTS")              