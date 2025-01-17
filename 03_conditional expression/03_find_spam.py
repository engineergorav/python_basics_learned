# spam key words
# click this ,buy this,subscribe me, make a lot of money

p1="Click this"
p2="Buy this"
p3="Subscribe me"
p4="Make lot of money"

message=input("enter your comment:  ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam:: ")
else:
    print("comment is not spam:  ")