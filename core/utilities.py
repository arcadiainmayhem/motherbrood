


#clamp between min and max
def clamp(value, low , high):
    #check if value is outside min or max
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value






#map values from 0 - 4095 to 0 - 1
def scale(value, orig_a, orig_b , new_a , new_b):
    percentage_original = (value - orig_a) / (orig_b - orig_a) 
    new_value = ((new_b -new_a) * percentage_original) + ( new_a )
    return new_value


#ignore small jitters in value
def deadband(reading , accepted, threshold ):
    if abs(reading - accepted) >= threshold:
        return reading
    else:
        return accepted


#wraparound counter change


#staleness check for silent bugs



#smoothing


#ratelimiting

