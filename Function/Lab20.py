# How to declare the Function

# Defination of Function
def getAdd(*values):
    print(type(values))

    sum=0
    for a in values:
        sum=sum+a
    return sum


output1=getAdd(10,20)
print(output1)

output2=getAdd(10,20,30)
print(output2)

output3=getAdd(10,20,30,40)
print(output3)


