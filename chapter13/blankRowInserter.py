import sys, openpyxl

try:
    n = int(sys.argv[1])
except:
    print('The first argument was not an integer.')
    sys.exit()

try:
    m = int(sys.argv[2])
except:
    print('The second argument was not an integer.')
    sys.exit()

source_workbook_filename = sys.argv[3]
try:
    source_workbook = openpyxl.load_workbook(source_workbook_filename)
    extension = '.' + source_workbook_filename.split('.')[-1]
except:
    print('The third argument was not a valid excel file.')    
    sys.exit()

source_workbook.active.insert_rows(n, m)

source_workbook.save(f'{source_workbook_filename.rstrip(extension)}_{n}_{m}{extension}')

source_workbook.close()