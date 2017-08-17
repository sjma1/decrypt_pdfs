#Seong Ma

import functions

'''
This program asks the user for a directory and a decryption key,
it will then use this key to decrypt all pdfs along the directory,
and notify the user whenever it succeeds or fails
'''

if __name__ == '__main__':
    functions.decrypt_pdfs(functions.get_directory(), functions.get_decryption())