# print elements of list using while loop

List = [
    42, 3.14, "hello", True, False, [1, 2, 3], (7, 8, 9),
    "python", 1024, 0.99, "GPT", -50, 2023, 5.5,
    "random", None, 88, 19.99, "AI", (3.1, 4.5),
    [100, 200], "list", 77, True, "variables", -1.23,
    False, 6.022e23, "science", "math"
]


i=0
while(i<len(List)):
    print(List[i])
    i+=1
