
import platform

MODE = "pi_remote"

#dev mode on Windows , live on Linunx
DEV_MODE =  platform.system() != "Linux"

MODES= {
    "installation" : {
        "launch_pd" : True,
        "open_bug_serial" : True,
        "open_panel_serial" : True,
        "osc_target_ip" : "127.0.0.1"
    },
    "pi_remote" : {
        "launch_pd" : False,
        "open_bug_serial" : True,
        "open_panel_serial" : True,
        "osc_target_ip" : "192.168.1.47"
    },
    "windows" : {
        "launch_pd" : False,
        "open_bug_serial" : False,
        "open_panel_serial" : True,
        "osc_target_ip" : "127.0.0.1"
    },
}

_m = MODES[MODE]
LAUNCH_PD = _m["launch_pd"]
OPEN_PANEL_SERIAL = _m["open_panel_serial"]
OPEN_BUG_SERIAL = _m["open_bug_serial"]
OSC_TARGET_IP = _m["osc_target_ip"]
#for troubleshooting
# WINDOWS_TARGET_IP = "192.168.1.47" 

#installation constants

AUDIO_DEVICE = "Headphones"
#USING HEADPHONES APPEARS AS CHANNEL 4 VIA -LISTdev


#audio channel can shift?
AUDIOCHANNEL = "1"





