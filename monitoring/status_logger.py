
import copy


REPORT_INTERVAL = 10

STATUS_REPORT ={

     "current_active_cicadas" :  None,
     "current_calling_cicadas" : 0,

     "cicada_messages_to_puredata" :  None,

     "panel_messages_to_puredata":  None,

     "current_button_press" : None,

     "current_active_gesture" :  None,

     "current_mother_mood" :  None,

     "current_zone_touched" :  None,
}





def get_snapshot():
    copy.deepcopy(STATUS_REPORT)
    return STATUS_REPORT