import pikepdf
from multiprocessing import Pool, cpu_count
import itertools

PDF_FILE = 'cracker4' \
'.pdf'
WORDLIST = 'pw_list.txt'

def try_password(password):
    password = password.strip()
    try:
        with pikepdf.open(PDF_FILE, password=password):
            return password
    except pikepdf.PasswordError:
        return None

def main():
    with open(WORDLIST, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.readlines()

    with Pool(cpu_count()) as pool:
        for result in pool.imap_unordered(try_password, passwords, chunksize=100):
            if result:
                print(f'Password found: {result}')
                pool.terminate()
                break
        else:
            print('Password not found.') 

if __name__ == '__main__':
    main()
