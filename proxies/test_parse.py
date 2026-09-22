from swamp.buglinkManager import BugLinkManager






buglink = BugLinkManager("COM3", 115200)




lines = {
 b"B,0,CALLING,0.83,1042",
 b"B,0,RISING,0.83,1042,.022",
 b"B,1,RISING,0.21,7",
 b"#booting",
 b"B,2,CALLING",
 b"garbage",
 b"B,0,CALLING,abc,1042",
 b"B,999,CALLING,0.83,1042"
 b""  
}




for line in lines:
    print(line, "-> " ,buglink._parse(line))