from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - given_date).days
    except ValueError:
        return None


print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2020-01-01"))
print(get_days_from_today("2099-12-31"))
print(get_days_from_today("не-дата"))
