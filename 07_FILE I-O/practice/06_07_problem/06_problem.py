#  check weather file contains "python or not or any other word"

import os
word=input(" enter which word you want ot find: ").strip()
def read_file():
    if not os.path.exists("log.txt"):
        print("this file doesn't exist")
    else:
        with open("log.txt","r") as f:
            content=f.read()
            if word.lower() in content.lower():
                print(f"yest this file contains the word '{word}'")
            else:
                print(f"no this file do not contanins the word '{word}'")
read_file()