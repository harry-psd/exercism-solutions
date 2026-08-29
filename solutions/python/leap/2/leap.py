def leap_year(year):
    """
    Function to check if the input year is a Leap Year or not.
    """
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
        return True
    return False