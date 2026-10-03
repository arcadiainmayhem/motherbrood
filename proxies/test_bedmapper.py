from swamp.bed.bedmapper import Bedmapper
from directors.swampbedDirector import SwampbedDirector


test_values = {
    "calling_count" : 15,
    "mean_arousal" : 4.50,
}


swampdirector = SwampbedDirector()
bedmapper = Bedmapper()


for i in range(10):
    bedmapper.update(test_values)