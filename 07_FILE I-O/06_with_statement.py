# f=open("file.txt")
# a=f.read()
# print(a)
# f.close()

# same can be written without f.close 
# by the help of with statement
with open("file.txt") as f:
    print(f.read())

# here i dont need to write f.close() explicitly