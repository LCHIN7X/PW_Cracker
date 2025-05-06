import PyPDF2

def crack_pdf(pdf_path, wordlist_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        if not reader.is_encrypted:
            print("PDF is not password protected.")
            return

        with open(wordlist_path, 'r') as words:
            for line in words:
                password = line.strip()
                try:
                    if reader.decrypt(password):
                        print(f"[+] Password found: {password}")
                        return
                except Exception as e:
                    pass
        print("[-] Password not found.")

crack_pdf("crack.pdf", "basic_list.txt")
