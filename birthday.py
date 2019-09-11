from datetime import datetime

def find_ending(day):
    number_endings = {
        1: 'st',
        2: 'nd',
        3: 'rd'
    }

    ending = ''
    if 10 < day < 20:
        ending = 'th'
    else:
        num = day % 10
        if num in number_endings:
            ending = number_endings.get(num)
        else:
            ending = 'th'
    return ending

if __name__ == '__main__':
    today = datetime.now()
    todays_day = today.day
    todays_day_ending = find_ending(todays_day)

    print(f"Today is the {todays_day}{todays_day_ending}")

    birthday_day = int(input("What day of the month is your birthday?" ))
    birthday_ending = find_ending(birthday_day)

    print(f"Your birthday is on the {birthday_day}{birthday_ending}!")