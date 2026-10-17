from panel.motherpanel import MotherPanel
from directors.panelDirector import PanelDirector
import traceback

class StubPd():
    def send ( self , target , value):
        print(f"[STUBPD] {target} , {value:.3f}")

motherPanel = MotherPanel()
puredataManager = StubPd()

panelDirector = PanelDirector(motherPanel , puredataManager)




# example frame
print("MOTHERPANEL START")
print("PANELDIRECTOR START")

testCount = 50

#packet , fw , potx 6 , buttons x 4
testframe = {
    "packetCount" : 5,
    "firmware": 1, 
    "pot1":250,
    "pot2":180,
    "pot3":2000,
    "pot4":500,
    "pot5":100,
    "pot6":0.6,
    "btn1":0,
    "btn2":1,
    "btn3":0
    }

try:



    for i in range(50):

        motherPanel.update(testframe)
        panelDirector.update()
        print(f"\n--- frame {i}")
        testframe["packetCount"] += 5
        testframe["pot1"] += 0.5
        testframe["pot2"] += 1
        testframe["btn1"] = i % 2
        




except Exception as e:
    traceback.print_exc()
    print(f"FRAME REJECTED : {e}")