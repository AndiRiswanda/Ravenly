waktu = "12:45:54AM"

'''
format 12 jam
conversi ke 24 jam
'''
def timeConversion(s):
    hour,minutes,second = s.split(":")
    second = second.replace("AM"  , "").replace("PM", "")
    if "PM" in s:
        hour = int(hour) + 12
        if hour == 24:
            hour = 12
    else:
        hour = int(hour)
        if hour == 12:
            hour = 0
    return(f"{hour:02}:{minutes}:{second}")
 


print (timeConversion(waktu))