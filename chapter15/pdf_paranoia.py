import os, PyPDF2, getpass
from pathlib import Path

password = getpass.getpass('Password:')

working_folder_path = r'C:\repos\python\automate_the_boring_stuff\chapter15\working_folder'

for folder, subfolders, filenames in os.walk(working_folder_path):
    folder_path = Path(folder)
    for source_file_path in folder_path.glob('*.pdf'):
        print('Encrypting ' + str(source_file_path))
        try:
            source_file = open(source_file_path, 'rb')
            source_file_reader = PyPDF2.PdfFileReader(source_file)
            
            if source_file_reader.isEncrypted:
                print('The file is already encrypted')
                continue

            pdf_file_writer = PyPDF2.PdfFileWriter()
            for pageNum in range(source_file_reader.numPages):
                pdf_file_writer.addPage(source_file_reader.getPage(pageNum))

            pdf_file_writer.encrypt(password)
            
            encrypted_file_path = folder_path / (source_file_path.stem + '_encrypted.pdf')
            encrypted_file = open(encrypted_file_path, 'wb')
            pdf_file_writer.write(encrypted_file)
            encrypted_file.close()
            print('Encryption Done')

            print('Starting Verification')
            encrypted_file = open(encrypted_file_path, 'rb')
            encrypted_file_reader = PyPDF2.PdfFileReader(encrypted_file)
            encrypted_file_reader.decrypt(password)
            for pageNum in range(source_file_reader.numPages):
                if source_file_reader.getPage(pageNum).extractText() != encrypted_file_reader.getPage(pageNum).extractText():
                    raise Exception()

            source_file.close()
            encrypted_file.close()
            print('Verification Done')

            print('Deleting source file')
            os.unlink(source_file_path)
        except:
            print('Encryption Failed')