
from swamp.buglinkManager import BugLinkManager
from swamp.broodswarm import Broodswarm
from swamp.cicadaConstants import BROOD_IDS
from hardware.hardwareConstants import UART_DEVICE, UART_BAUD


buglink = BugLinkManager( "COM3" , UART_BAUD)


#need to test incoming message from ESPMOTHER