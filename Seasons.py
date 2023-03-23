def get_season(month_str, day):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    try:
        month = months[month_str]
    except KeyError:
        return "Invalid"
    
    days_in_month = {
        1: 31,
        2: 29, #Leap year not considered 
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if day < 1 or day > days_in_month[month]:
        return "Invalid"
    
    if (month == 3 and day >= 20) or (month > 3 and month < 6) or (month == 6 and day <= 20):
        return "Spring"
    elif (month == 6 and day >= 21) or (month > 6 and month < 9) or (month == 9 and day <= 21):
        return "Summer"
    elif (month == 9 and day >= 22) or (month > 9 and month < 12) or (month == 12 and day <= 20):
        return "Fall"
    else:
        return "Winter"

month_str = input("Enter a month: ")
day = int(input("Enter a day: "))
season = get_season(month_str, day)
print(season)
