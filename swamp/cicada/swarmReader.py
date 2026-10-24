

from swamp.cicada.cicadaConstants import SWARM_DENSITY_PEAK_HIGH_THRESHOLD , SWARM_DENSITY_PEAK_LOW_THRESHOLD
from swamp.bed.swampbedConstants import BED_CONTINUOUS, BED_EVENTS
import statistics
from core.utilities import clamp


#continous
#density  tension rest unrest

class SwarmReader():

    def __init__(self,broodswarm):

        self.broodswarm = broodswarm
        #flag for events - swarm density
        self.peak_armed = True

        self.readers = {
            "density" : self.density,
            "tension" : self.tension,
            "rest" : self.rest,
            "unrest" : self.unrest,
        }

    def read(self,now):
        values = {}
        for name in BED_CONTINUOUS:
            values[name] = self.readers[name](now)
        return values

    def events(self,now):
        events = []

        for bug_id in self.broodswarm.get_and_drain_call_onsets():
            events.append(("call_onset",bug_id))
        if self.swarm_peak(now):
            events.append(("swarm_peak",1))
        return events
    
    #-- CONTINUOUS 

    #uses time to check exact
    def density(self , now):
        active_bugs = self.broodswarm.active_count(now)

        if active_bugs == 0:
            return 0.0
        
        bugs_in_calling = self.broodswarm.calling_count(now)

        current_density = bugs_in_calling / active_bugs

        return current_density




    def tension(self , now):
        return self.broodswarm.mean_arousal(now)



    def rest(self,now):
        active_bugs = self.broodswarm.active_count(now)
        

        if active_bugs == 0:
            return 0.0
        
        resting_bugs = self.broodswarm.bugs_at_rest(now)
        #float value
        bugs_at_rest = resting_bugs / active_bugs

        return bugs_at_rest


    #spread of arousal 
    def unrest(self,now):
        active_bugs = self.broodswarm._active_bugs(now)

        current_arousal_value = []

        for row in active_bugs:
            current_arousal_value.append(row["arousal"])

        if current_arousal_value == []:
            return 0.0
        

        standard_deviation = statistics.pstdev(current_arousal_value)

        unrest_value = clamp(standard_deviation * 2 , 0 , 1)

        return unrest_value 

    #----Events

    def swarm_peak(self,now):

        current_density = self.density(now)
        if self.peak_armed == True and current_density > SWARM_DENSITY_PEAK_HIGH_THRESHOLD:
            self.peak_armed = False
            return True
        elif self.peak_armed == False and current_density < SWARM_DENSITY_PEAK_LOW_THRESHOLD:
            self.peak_armed = True
            return False
        else:
            return False
