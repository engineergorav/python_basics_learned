
def fun():
    try:
        ans=int(input("enter a number:"))
        return(ans)
    except Exception :
        return("please enter only integer: ")
    finally:
        return("thank you: ")
print(fun())