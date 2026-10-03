
from directors.swampbedDirector import SwampbedDirector
import time

def main():

    #start
    swampbed = SwampbedDirector()



    try:    
        if not swampbed.start(): #if not true
            print("[MAIN] SWAMPBED not started successfully")
            return 

        print("[MAIN] Swampbed Started Successfully ")     

        while True:

            now = time.monotonic()
            swampbed.tick(now)           


    except KeyboardInterrupt:
        #stop
        pass

    finally:
        swampbed.stop()
        print("[MAIN] Swamp Stopped")

if __name__ == "__main__":
    main()