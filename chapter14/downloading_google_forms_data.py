import ezsheets

google_spreadsheet_id = '1X3oaZq8sUcqN5DrpKt3mSC8afvz4PryPgM20Ibj-N6Q'

google_spreadsheet = ezsheets.Spreadsheet(google_spreadsheet_id)

reponses_sheet = google_spreadsheet['Form responses 1']

mails = {mail for mail in reponses_sheet.getColumn(3)[1:] if mail != ''}

print(mails)