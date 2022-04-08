with open("data.txt") as test:
    lines = test.readline()

DAYS_IN_A_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Mozna tez uzyc wbudowanej biblioteki calendar - import calendar i funkcja isleapyear()


def checkdate():
    print("Given only the year the function returns an answer True/False if the given year is leap or not.\n"
          "Given year and month the function returns an answer 'how many days are in given month in particular year'"
          "Given a full date, the function returns information which day of the year is a given day\n"
          "Provide a year/ year + month or full date in YYYY/M/DD format ")

    # date = input("Provide a year/ year + month or full date in YYYY/M/DD format ")
    date = lines
    new_date = date.split("/")
    year = int(new_date[0])

    if len(date) <= 4:
        if ((year % 400 == 0) or
                (year % 100 != 0) and
                (year % 4 == 0)):
            return "Given year is a leap Year"
        else:
            return "Given year is not a leap year"
    elif len(date) == 6:
        month = int(new_date[1]) - 1
        return DAYS_IN_A_MONTHS[month]
    else:
        day_in_year = []
        month = int(new_date[1]) - 1
        day = int(new_date[2])
        for index in range(month + 1):
            day_in_year.append(DAYS_IN_A_MONTHS[index])
        if month == 11:
            return sum(day_in_year) + day - 31
        else:
            return sum(day_in_year) + day

# Na pewno mozna bylo tutaj sprawdzac inne formaty daty -> znalazlem biblioteke re,
# ktora przy funkcji split powinna przyjmowac wiecej znakow
# Problem 2. data u mnie przyhmuje forma rok miesiac ->
print(checkdate())
