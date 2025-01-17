# write a program to generate multiplication table from 2 to 20 and write it to the different files place these files 
# in a folder for 13 year old 

def write_table(n):
    table=""
    for i in range(1,11):
        table+=f"{n} X {i} = {n*i}\n"
    with open(f"TABLE/table_{n}.txt","w") as f:
        f.write(table + '\n')
for i in range(2,21):
    write_table(i)