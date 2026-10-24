
from swamp.broodswarm import Broodswarm


#continous
#density  tension rest unrest

class CicadaIntepreter():

    def __init__(self,broodswarm):

        self.broodswarm = broodswarm
        

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
        return self.broodswarm.mean_arousal



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
        active_bugs = self.broodswarm._active_bugs

        arousal_value = []
        
        for row in active_bugs:
            arousal_value.append(row["arousal"])






    #----Events
    def call_onset(self ,now ):
        return self.broodswarm._active_bugs["just_calling_state"]


    def swarm_density(self,now):
        SWARM_DENSITY_THRESHOLD = 0.60
        current_density = self.density(now)
        if current_density > SWARM_DENSITY_THRESHOLD:
            return True
