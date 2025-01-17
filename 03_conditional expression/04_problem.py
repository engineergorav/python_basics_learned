# tell weather user name contains less than 10 characters

username=input("enter the user name, do not exceed it more than 10 words:   ")


if(len(username)>10):
    print("please rewrite the user name, because it exceeded the limit of 10 characters   ")
else:
    print("you have entered correct username, this is axcepted:  ")