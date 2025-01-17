# same as switch in c++
def numb(n):
    match n:
        case 200:
            return "ok"
        case 300:
            return "no"
        case 303030:
            return "bilkulno"
        case _:
            return "unknown status"
ans = int(input("enter:"))
print(numb(ans))
