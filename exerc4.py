from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []
    for user in users:
        birthday = datetime.strptime(user["birthday", "%Y.%m.%d"]).date()
        birthday_this_year = birthday.replace(year=today.year + 1)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            days_until_birthday = (birthday_this_year - today).days
            if 0 <= days_until_birthday <= 7:
                congratulation_data = birthday_this_year 
                if congratulation_data.weekday() == 5:
                    congratulation_date += timedelta(days=1)
                    result.append({
                        "name": user["name"],
                        "congratulation_date": congratulation_date.strftime("&Y.%m.%d")
                    })
                    return result
                users = [
    {"name": "John Doe", "birthday": "1985.06.16"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
                upcoming_birthdays = get_upcoming_birthdays(users)
print(get_upcoming_birthdays)

