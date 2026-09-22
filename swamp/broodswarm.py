from swamp.cicadaConstants import BROOD_TIMEOUT

class Broodswarm:

    def __init__(self , brood_ids):
        #container for cicadas
        self.broodlings = {}

        #initialise broodlings

        for broodling in brood_ids:

            self.broodlings[broodling] = {
                
                "state": None,

                "arousal": None,

                "seq" : None,




                
                "last_seen" : None,


            }






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

    

    def seen_recently(self, brood_id , now):

        row = self.broodlings[brood_id]

        #guard against None error
        if row["last_seen"] is None:
            return False

        age = now - row["last_seen"]
        
        return age < BROOD_TIMEOUT



    #what would director ask for