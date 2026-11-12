
from core.installationConstants import DEV_MODE

HARDWARE = {
    "pi": {
        "pd_binary": "/usr/local/bin/pd",

        "pd_externals_path": "/home/arcadia/Documents/else",
        "pd_externals_parent": "/home/arcadia/Documents",
        "pd_audio_device": "snd_rpi_hifiberry_dacplus (plug-in)",

        #commented out because of by-id confliced
        #"mother_port": "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0", #ESP32 C3 SUPERMINI  - MOTHER 
        #"panel_port": "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0", #ESP32 38 PIN - PANEL



        #using by path
        "mother_port": "/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0", #ESP32 C3 SUPERMINI  - MOTHER 
        "panel_port" : "/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.4:1.0-port0", #ESP32 38PIN PANEL 
        "led_port": "/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.4:1.0-port0",#ESP32 38PIN LED 
    },


    "windows" : {
        "pd_binary": "pd",
        "pd_externals_path": "",
        "pd_audio_device": "",
        "mother_port": "COM3",
        "panel_port": "COM4",
        "led_port": "COM5",
    }

}

_h = HARDWARE["windows" if DEV_MODE else "pi"]
PD_BINARY = _h["pd_binary"]
PD_EXTERNALS_PATH = _h["pd_externals_path"]
PD_EXTERNALS_PARENT = _h["pd_externals_parent"]
PD_AUDIO_DEVICE_NAME = _h["pd_audio_device"]
MOTHER_PORT    = _h["mother_port"]
MOTHER_PANEL_PORT = _h["panel_port"]
MOTHER_LED_PORT   = _h["led_port"]


# if DEV_MODE:
#     PD_BINARY = "pd"            # placeholder, never launched
#     PD_EXTERNALS_PATH = ""
#     MOTHER_PORT = "COM3"        # your real ones from Device Manager
#     MOTHER_PANEL_PORT = "COM4"
#     PD_AUDIO_DEVICE_NAME = ""
# else:
#     PD_BINARY = "/usr/local/bin/pd"
#     PD_AUDIO_DEVICE_NAME = "snd_rpi_hifiberry_dacplus (plug-in)"
#     PD_EXTERNALS_PATH = "/home/arcadia/Documents/else"
#     PD_EXTERNALS_PARENT = "/home/arcadia/Documents"
#     MOTHER_PANEL_PORT = "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0" #ESP32 38 PIN - PANEL
#     MOTHER_PORT = "/dev/serial/by-id/usb-Espressif_USB_JTAG_serial_debug_unit_30:ED:A0:65:9C:D0-if00" #ESP32 C3 SUPERMINI  - MOTHER 
#     #ESP32 LED

#UART COMMS
UART_DEVICE = "/dev/serial0"
UART_BAUD = 115200


MOTHER_BAUD = 115200

#PI GPIO WIRING
PI_RX = 15
PI_TX = 14



ESP_MAC_ADDR = {}


# MOTHER_ESP_MAC_ADDR = {0x00, 0x70, 0x07, 0x7E, 0x4A, 0x94} [BIGGED ESP]
MOTHER_ESP_MAC_ADDR = [0x30, 0xED, 0xA0, 0x65, 0x9C, 0xD0]