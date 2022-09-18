import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

for row_number in range(2, ss[0].getColumn(3).index('') + 1):
    if int(ss[0].getRow(row_number)[0]) * int(ss[0].getRow(row_number)[1]) == int(ss[0].getRow(row_number)[2]):
        continue
    print('Mistake on row: ' + str(row_number)) 