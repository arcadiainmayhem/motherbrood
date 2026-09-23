from swamp.puredataManager import PuredataManager
from swamp.swampbedConstants import BED_OSC_PORT
from swamp.patches.patchlibrary import TEST_PATCH
from core.installationConstants import DEV_MODE , AUDIO_DEVICE , AUDIOCHANNEL







pd_m = PuredataManager(TEST_PATCH, AUDIO_DEVICE , BED_OSC_PORT)

audio_device = pd_m._find_audio_device()



print(audio_device)