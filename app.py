import random
import pyautogui

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ"

allchar = list(chars)

pw = pyautogui.password('Enter a password:')
sample_password = " "

while (sample_password != pw):
    sample_password = random.choices(allchar,k=len(pw))

    print(str(sample_password))

    if (sample_password == list(pw)):

        print("Your password is:" +"".join(sample_password))

        break