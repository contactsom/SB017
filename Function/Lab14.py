# How to declare the Function

# Defination of Function
def getMyNameFunction(initial,firstName,lastName):
    print("Initail :",initial)
    print("firstName :",firstName)
    print("lastName :",lastName)

    fullName=initial+firstName+" "+lastName
    return fullName


# Caller
name=getMyNameFunction("Mrs. ","Donnita","Mennealy")
print(name)





