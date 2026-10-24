from swamp.cicada.cicadaConstants import BROOD_TIMEOUT , BUG_FRAME , CICADASTATES , CALLING_HOLD

class Broodswarm:

    def __init__(self , brood_ids):
        #container for cicadas
        self.broodlings = {}
        self.call_onsets = []
        #initialise broodlings

        for broodling in brood_ids:

            row = {}
            self.broodlings[broodling] = row

            for name in BUG_FRAME:
                #skip id
                if name != "id":
                    row[name] = None

            row["last_seen"] = None

        

    def update(self , frame, now):
        #check incoming value under key - id
        
        brood_id = frame["id"]
        


        #return if id is not 
        if brood_id not in self.broodlings:
            return 


        #check against row for correct broodling to update based on id
        row = self.broodlings[brood_id]
        
        
        previous_state = row["state"]
        #check through incoming frame 
        for name in frame:
            if name != "id":
                row[name] = frame[name]


        #time specific
        row["last_seen"] = now



        #after copying
        current_state = row["state"]

        if row["state"] == CICADASTATES["STATE_CALLING"]:
            row["last_calling"] = now

        #check against previous state for change
        if current_state != previous_state:
            #statechange
            if current_state== CICADASTATES["STATE_CALLING"]:
                self.call_onsets.append(brood_id)

        

    #return values of broodlings

    def seen_recently(self, brood_id , now):

        row = self.broodlings[brood_id]

        #guard against None error
        if row["last_seen"] is None:
            return False

        age = now - row["last_seen"]
        
        return age < BROOD_TIMEOUT


    
    #what else would director ask for

    #CHECK BUGS FOR STATE CALLING
    def calling_count(self, now):
        count = 0
        for row in self._active_bugs(now):
            t = row.get("last_calling")
            if t is not None and (now - t) < CALLING_HOLD:
                count += 1
        return count

    #CHECK BUGS FOR STATE REFACTORY
    def bugs_at_rest(self,now):
        rest_count = 0
        for row in self._active_bugs(now):
            if row["state"] == CICADASTATES["STATE_REFRACTORY"]:
                rest_count += 1
        return rest_count




    def mean_arousal(self , now):
        arousal = 0
        
        rows = self._active_bugs(now)

        if not rows:
            #print("[BROODSWARM] NO ACTIVE BUGS TO CALCULATE AROUSAL")
            return 0.0 #because float

        count = len(rows)

        for i in range(count):
            arousal += rows[i]["arousal"] 

        mean_arousal = arousal / count

        return mean_arousal




    def active_count(self, now):
        total = len(self._active_bugs(now)) #returns int
        return total

    def _active_bugs(self, now ):

    
        active_rows_of_bugs = []
        #loop through total swarm + check seen recently
        for brood in self.broodlings:
            if (self.seen_recently(brood, now)):
                #seen recently
                active_rows_of_bugs.append(self.broodlings[brood])

        return active_rows_of_bugs


    def get_and_drain_call_onsets(self):
        onset = self.call_onsets
        self.call_onsets = []
        return onset