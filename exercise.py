from datetime import datetime
def get_days_from_today(date_str: str) -> int:
    """
    Calculate the number of days from today to the given date.
    Parameters:
    date (str): A date string in the format 'YYYY-MM-DD'.
    Returns:
    int: The number of days from today to the given date.
    """

    input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    today = datetime.datetime.today()
    delta = today.date() - input_date.date()
    return delta.days
    
    print(get_days_from_today("2025-06-20"))

