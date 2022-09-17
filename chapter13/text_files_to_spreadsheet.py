import openpyxl


text_files_paths = ['contentA.txt', 'contentB.txt', 'contentC.txt', 'contentD.txt', 'contentE.txt']

workbook = openpyxl.Workbook()
active_sheet = workbook.active

for text_file_index, text_file_path in enumerate(text_files_paths):
    text_file = open(text_file_path, 'r')
    for line_index, line in enumerate(text_file.readlines()):
        active_sheet.cell(line_index + 1, text_file_index + 1).value = line

workbook.save('text_files_to_spreadsheet.xlsx')