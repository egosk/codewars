# task:
# Your task in order to complete this Kata is to write a function which formats a duration,
# given as a number of seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years,
# days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#
# format_duration(62)    # returns "1 minute and 2 seconds"
# format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

def format_duration(seconds):
    if seconds ==0:
        return "now"

    s = 1
    minute = 60 * s
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day # 31536000
    duration_dict = {"seconds": 0, "minutes": 0, "hours" :0, "days": 0, "years": 0}

    if seconds >= year:
        duration_dict['years'], seconds = divmod(seconds, year)
    if seconds >= day:
        duration_dict['days'], seconds = divmod(seconds, day)
    if seconds >= hour:
        duration_dict['hours'], seconds = divmod(seconds, hour)
    if seconds >= minute:
        duration_dict['minutes'], seconds = divmod(seconds, minute)
    duration_dict['seconds'] = seconds

    formula = ''
    formulas = []
    for key, val in duration_dict.items():
        if val ==1:
            formulas.append(str(val) + ' ' + key[:-1])
        elif val >= 1:
            formulas.append(str(val) + ' ' + key)


    for f in formulas:
        if formulas.index(f) == 0:
            formula = f
        if formulas.index(f) == 1:
            formula = f + ' and ' + formula
        if formulas.index(f) > 1:
            formula = f + ', ' + formula

    return formula

format_duration(31536005)