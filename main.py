import fitz
from tqdm import tqdm

def crack_pdf(pdf_path, password_list):

    doc = fitz.open(pdf_path)

    for password in tqdm(password_list, "Guessing password"):

        if doc.authenticate(password):

            return password
        
    return None

        
if __name__ == "__main__":
    import sys
    pdf_filename = "cracker4.pdf"
    wordlist_filename = "rockyou.txt"

    try:
        with open(wordlist_filename, "r", errors="replace") as f:
            passwords = f.read().splitlines()
    except Exception as e:
        print(f"Error reading wordlist file: {e}")
        sys.exit(1)

    password = crack_pdf(pdf_filename, passwords)
    if password:
        print(f"Password is: {password}")
    else:
        print("Password not found.")

        

