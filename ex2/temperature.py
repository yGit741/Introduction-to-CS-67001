#################################################################
# FILE : calculate_mathematical_expression
# WRITER : Yonatan Greenshpan  , yonatan_green , 204266191
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Helping Hagrid decide if it is summer yet.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: -
# NOTES: -
#################################################################

def is_it_summer_yet(threshold, temp1, temp2, temp3):
    """This function get temperature threshold and three temperature measures
     and return true if there are at least two sequence days with temperatures
     above the threshold and False if not."""
    if temp1 > threshold:
        if temp2 > threshold:
            return True
    elif temp2 > threshold:
        if temp3 > threshold:
            return True
    return False


