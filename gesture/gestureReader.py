from gesture.gestureConstants import QUIET_GAP , MAX_CONVERSATION_WINDOW_INTERVAL  ,  GESTUREPARAMS, GESTURE_RULES
from mood.moodConstants import GESTURES

class GestureReader():

    #each press starts conversation
    
    def __init__(self):
        


        self.presses = []#array of tuples store current presses

        self.startTime = None
        self.lastPressTime = None
        
        #raise error if limit isnt inparams
        for x in GESTURE_RULES: #loop through gesture keys
            for limit in GESTURE_RULES[x]:
                if limit not in GESTUREPARAMS:
                    raise KeyError(f"[GESTUREREADER] {limit} not in GestureParams")
                
    def update(self , now):
        #nothing in progress, nothing to check
        if not self.presses:
            return
        
        #calls method to check 

        #if pass gap , close ( visitor stop )
        stoppedPressing = ( now - self.lastPressTime > QUIET_GAP)
        #checks every loop , if max window interval, calls close current conversation window
        tooLong= ( now - self.startTime > MAX_CONVERSATION_WINDOW_INTERVAL)

        if stoppedPressing or tooLong:
            print(f"[GESTUREREADER] Timeout! Conversation Closing")
            return self.close_conversation()


    def on_press(self , key , now):

        #if first press, start timer
        if not self.presses:
            self.startTime = now
        #add to buffer, 
        #should take valid presses from panel director ( passed down ) 

        self.presses.append((key , now)) #using tuple, [ ( x , y ) , ( x2 , y2)]

        self.lastPressTime = now

       #print(f"[GESTUREREADER] Current Button Press {key}, {now}")


        print(f"[GESTUREREADER] Current Set of Presses : {self.presses}")



    def close_conversation(self):
        
        keys = []
        times = []

        #unpack tuple into two lists
        for press in self.presses:
            key = press[0]
            t = press[1] # cause tuple

            keys.append(key)
            times.append(t)

        #checking count
        count = len(keys)

        distinct = len(set(keys))

        #check time
        firstTime = times[0] 
        lastTime = times[len(times) - 1]
        span =  lastTime - firstTime

        #check gaps
        gaps = []

        for i in range(len(times)-1):
            thisTime = times[i]
            nextTime = times[i + 1]
            gaps.append(nextTime - thisTime)

        #calculate

        if len(gaps) > 0:
            total = 0
            for g in gaps:
                total = total + g
            average = total / len(gaps)
        else:
            average = 0.0


        gesture = self._classify_presses(count , distinct , span , average)

        print(f"[GESTUREREADER] keys={keys} count={count} distinct={distinct} "
            f"span={span:.1f}s gap={average:.2f}s → {gesture}")
        #reset
        self.presses = []
        self.startTime = None
        self.lastPressTime = None

        return gesture

    def _rule_matches(self , rule , incoming ):

        #COUNT
        if "min_count" in rule and incoming["count"] < rule["min_count"]:
            return False
        if "max_count" in rule and incoming["count"] > rule["max_count"]:
            return False
        
        #DISTINCT
        if "min_distinct" in rule and incoming["distinct"] < rule["min_distinct"]:
            return False
        if "max_distinct" in rule and incoming["distinct"] > rule["max_distinct"]:
            return False

        #SPAN
        if "min_span" in rule and incoming["span"] < rule["min_span"]:
            return False
        if "max_span" in rule and incoming["span"] > rule["max_span"]:
            return False

        #GAP
        if "min_gap" in rule and incoming["gap"] < rule["min_gap"]:
            return False
        if "max_gap" in rule and incoming["gap"] > rule["max_gap"]:
            return False

        return True
    
    def _classify_presses(self , count, distinct, span , gap):

    
        #store incoming

        incoming_params = {
            "count" : count,
            "distinct" : distinct,
            "span" : span,
            "gap" : gap
        }



        for gesture, rule in GESTURE_RULES.items():
            if self._rule_matches(rule , incoming_params):
                return gesture

        return None
