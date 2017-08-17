import os, PyPDF2, send2trash


def get_directory():
    while True:
        directory = input("Input directory: ")
        if os.path.isdir(directory):
            return directory
        print('INVALID PATH\n')
        
def get_decryption():
    return input("Enter the decryption key: ")

def append_to_filename(filename):
    return filename.split('.pdf')[0] + '_decrypted.pdf'


def write_to_pdf(new_file, pdf_writer, pdf_reader):
    for page_number in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_number))
    pdf_writer.write(new_file)


def decrypt_pdfs(directory, decryption):
    for dir_name, subdir_list, file_list in os.walk(directory):
        for filename in file_list:
            if filename.endswith('.pdf'):                               
                absolute_directory = os.path.abspath(dir_name)
                absolute_filename  = os.path.join(absolute_directory, filename)
                absolute_file      = open(absolute_filename, 'rb')
                os.chdir(absolute_directory)
                pdf_reader = PyPDF2.PdfFileReader(absolute_file)
                if pdf_reader.isEncrypted:
                    print("DECRYPTING: " + absolute_filename)
                    if pdf_reader.decrypt(decryption) == 1:
                        print("SUCCESSFUL DECRYPTION\n\n")
                        pdf_writer = PyPDF2.PdfFileWriter()
                        new_file   = open(append_to_filename(absolute_filename), 'wb')
                        write_to_pdf(new_file, pdf_writer, pdf_reader)
                        absolute_file.close()
                        new_file.close()
                        send2trash.send2trash(absolute_filename)
                    else:
                        print("FAILED TO DECRYPT\n\n")
                absolute_file.close()