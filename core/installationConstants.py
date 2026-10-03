
import platform


#dev mode on Windows , live on Linunx
DEV_MODE =  platform.system() != "Linux"
LAUNCH_PD = not DEV_MODE  #true if on PI

#installation constants

AUDIO_DEVICE = "Headphones"
#USING HEADPHONES APPEARS AS CHANNEL 4 VIA -LISTdev


#audio channel can shift?
AUDIOCHANNEL = "1"





