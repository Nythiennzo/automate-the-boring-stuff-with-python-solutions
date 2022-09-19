import os, PyPDF2, getpass
from pathlib import Path

password = getpass.getpass('Password:')

working_folder_path = r'C:\repos\python\automate_the_boring_stuff\chapter15\working_folder'

for folder, subfolders, filenames in os.walk(working_folder_path):
    folder_path = Path(folder)
    for source_file_path in folder_path.glob('*_encrypted.pdf'):
        print('Decrypting ' + str(source_file_path))
        try:
            source_file = open(source_file_path, 'rb')
            source_file_reader = PyPDF2.PdfFileReader(source_file)
            
            if not source_file_reader.isEncrypted:
                print('The file is already not encrypted')
                continue

            source_file_reader.decrypt(password)

            pdf_file_writer = PyPDF2.PdfFileWriter()
            for pageNum in range(source_file_reader.numPages):
                pdf_file_writer.addPage(source_file_reader.getPage(pageNum))
            
            decrypted_file_path = folder_path / (source_file_path.name.rstrip('_encrypted.pdf') + '.pdf')
            decrypted_file = open(decrypted_file_path, 'wb')
            pdf_file_writer.write(decrypted_file)
            decrypted_file.close()
            source_file.close()
            print('Decryption Done')
        except:
            print('Decryption Failed')