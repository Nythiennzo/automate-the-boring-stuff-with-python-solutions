import re


input_text = '29/02/2100'

date_re = re.compile('(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/([12]\d{3})')
mo = date_re.search(input_text)

try:
    day, month, year = mo.groups()

    print('day:' + day)
    print('month:' + month)
    print('year:' + year)

    day_int = int(day)
    year_int = int(year)

    is_leap_year = year_int % 400 == 0 or year_int % 4 == 0 and year_int % 100 != 0

    if (month in ('04', '06', '09', '11') and day_int == 31) or (month == '02' and day_int > 28 + is_leap_year):
        print('Date is invalid')
    else:
        print('Date is valid')

except:
    print('Date not detected')