def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        return "Freezing"
    elif temp<11:
        return "Very Cold"
    elif temp>=11 and  temp<21:
        return "Cold"
    elif temp>=21 and temp<31:
        return "Normal"
    elif temp>30 and temp<41:
        return "Hot"
    else: 
        return "Very Hot"