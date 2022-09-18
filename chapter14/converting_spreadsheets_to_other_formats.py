#The library does not seem to work anymore for uploading
import ezsheets, sys

filename = sys.argv[1]
target_format = sys.argv[2]

google_spreadsheet = ezsheets.upload(filename)

match target_format:
    case 'csv':
        google_spreadsheet.downloadAsCSV()
    case 'excel':
        google_spreadsheet.downloadAsExcel()
    case 'html':
        google_spreadsheet.downloadAsHTML()
    case 'ods':
        google_spreadsheet.downloadAsODS()
    case 'pdf':
        google_spreadsheet.downloadAsPDF()
    case 'tsv':
        google_spreadsheet.downloadAsTSV()
    case _:
        print('Format is invalid')
    

