


#UART COMMS
UART_DEVICE = "/dev/serial0"
UART_BAUD = 115200

MOTHER_PANEL_PORT = "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0" #ESP32 38 PIN

MOTHER_PORT = "/dev/serial/by-id/usb-Espressif_USB_JTAG_serial_debug_unit_30:ED:A0:65:9C:D0-if00" #ESP32 C3 SUPERMINI

MOTHER_BAUD = 115200

#PI GPIO WIRING
PI_RX = 15
PI_TX = 14

PD_BINARY = "/usr/local/bin/pd"
PD_EXTERNALS_PATH = "/home/arcadia/Documents/else"

PD_AUDIO_DEVICE_NAME = "snd_rpi_hifiberry_dacplus (plug-in)"

ESP_MAC_ADDR = {}


# MOTHER_ESP_MAC_ADDR = {0x00, 0x70, 0x07, 0x7E, 0x4A, 0x94} [BIGGED ESP]
MOTHER_ESP_MAC_ADDR = {0x30, 0xED, 0xA0, 0x65, 0x9C, 0xD0}