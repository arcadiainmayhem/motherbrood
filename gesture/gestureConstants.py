from mood.moodConstants import GESTURES


QUIET_GAP = 1.5
MAX_CONVERSATION_WINDOW_INTERVAL = 6

#count , distinct , span , gap

GESTUREPARAMS = {
    "min_count",
    "max_count",
    "min_distinct",
    "max_distinct",
    "min_gap",
    "max_gap",
    "min_span",
    "max_span",
}

GESTURE_RULES = {
    GESTURES.SPEAK: {
        "min_count" : 6 , "max_gap" : 0.3, "min_distinct": 2
    },
    GESTURES.OFFER:   {
        "min_distinct": 3 ,
    },
    GESTURES.POKE:   {
        "max_count": 3 ,
    },
}