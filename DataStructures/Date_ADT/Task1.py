
__author__ = 'Gabriel Ugolole'

# checkdates.py

from date import Date
from linearbag import Bag


def main():
    # Date before which a person must have been born to be 21 or older
    bornBefore = Date(6, 1, 1988)
    bag = Bag()
    # Extract dates from the user and place them in the bag

    date = promptAndExtractDate()
    while date is not None:
        bag.add(date)
        date = promptAndExtractDate()

    # Checks those items less than 21 years
    for date in bag:
        if date <= bornBefore:
            print("Is at least 21 years of age")


def promptAndExtractDate():
    print('Enter your birthday: ')
    month = int(input("month (0 and quit): "))
    if month == 0:
        return None
    else:
        day = int(input('Day: '))
        year = int(input('year: '))
        return Date(month, day, year)

main()
