from swamp.cicadaConstants import BROOD_TIMEOUT , BUG_FRAME , CICADASTATES

class Broodswarm:

    def __init__(self , brood_ids):
        #container for cicadas
        self.broodlings = {}

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
        #check through incoming frame 
        for name in frame:
            if name != "id":
                row[name] = frame[name]


        #time specific
        row["last_seen"] = now

    #return values of broodlings

    def seen_recently(self, brood_id , now):

        row = self.broodlings[brood_id]

        #guard against None error
        if row["last_seen"] is None:
            return False

        age = now - row["last_seen"]
        
        return age < BROOD_TIMEOUT


    
    #what else would director ask for


    def calling_count(self , now):

        count = 0
        
        for row in self._active_bugs(now):
            if (row["state"] == CICADASTATES["STATE_CALLING"]) : #states arrive as int rising -calling - refractory 
                count += 1

        return count

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
