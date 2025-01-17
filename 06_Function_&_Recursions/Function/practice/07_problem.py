# write a program to remove a given word form a list and strip it at the same time 

def remove(l,word):
    new_list=[]
    for item in l:
        if(item!=word):
            new_list.append(item.strip(word))
    return new_list

l=["rohan","rajan","kiran","viran","hiran"]

word=input("enter word: ")

print(remove(l,word))