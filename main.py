
from directors.swampbedDirector import SwampbedDirector

def main():

    #start
    swampbed = SwampbedDirector()

    if swampbed.start():
        print("[MAIN] SWAMPBED not started successfully")
        return 

    print("[MAIN] Swampbed Started Successfully ")

    try:         
        while True:
            
            swampbed.tick()           


    except KeyboardInterrupt:
        #stop
        pass

    finally:
        swampbed.stop()
        print("[MAIN] Swamp Stopped")

if __name__ == "__main__":
    main()