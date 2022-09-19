import sys, PyPDF2

dictionary_file = open('dictionary.txt')
words = [word.rstrip('\n') for word in dictionary_file.readlines()]
dictionary_file.close()

try:
    encrypted_pdf_file = PyPDF2.PdfFileReader(sys.argv[1])
except:
    print('There was a problem loading the file.')

if not encrypted_pdf_file.isEncrypted:
    print('The file is not encrypted.')
    sys.exit()

password = None

for word in words:
    if encrypted_pdf_file.decrypt(word):
        password = word
        break
    
    lower_word = word.lower()
    if encrypted_pdf_file.decrypt(lower_word):
        password = lower_word
        break

    capitalize_word = word.capitalize()
    if encrypted_pdf_file.decrypt(capitalize_word):
        password = capitalize_word
        break

if password:
    print('The password is ' + password)
else:
    print('The password could be found.')