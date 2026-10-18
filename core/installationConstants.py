
import platform


#dev mode on Windows , live on Linunx
DEV_MODE =  platform.system() != "Linux"
LAUNCH_PD = not DEV_MODE  #true if on PI

PI_REMOTE = {
    "launch_pd" : False,
    "open_bug_serial" : True,
    "open_panel_serial" : True,
    "osc_target_ip" : "192.168.1.47"
}

OPEN_PANEL_SERIAL = True
OPEN_BUG_SERIAL = True

OSC_TARGET_IP = "127.0.0.1"
#for troubleshooting
WINDOWS_TARGET_IP = "192.168.1.47" 

#installation constants

AUDIO_DEVICE = "Headphones"
#USING HEADPHONES APPEARS AS CHANNEL 4 VIA -LISTdev


#audio channel can shift?
AUDIOCHANNEL = "1"





