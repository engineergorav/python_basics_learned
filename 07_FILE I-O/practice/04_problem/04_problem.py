# a file contains word "donkey" multiple times, You need to write a which replace this word
#  with "####" by updating the same file

import os
word=input("Type the word to be replaced:  ").strip()
word_1=input("Type the word for replacement: ").strip()
def read_file():
    if not os.path.exists("file.txt"):
        print("no such a file exists, please recheck the file name ! ")
    else:
        with open("file.txt",) as f:
            readed_file=f.read()
            readed_content=readed_file.lower()
            word_in_lower=word.lower()
            if(word_in_lower in readed_content):
                updated_content=""
                for original_word in readed_content.split():
                    if original_word.lower()==word_in_lower:
                        updated_content+=word_1+" "
                    else:
                        updated_content+=original_word +" " 
                update_file(updated_content.strip())
            else:
                print("Everything is absolutely correct: ")
def update_file(string):
    with open("file.txt","w") as f:
        f.writelines(string)
        print("Changes have been made successfully: ")

read_file()