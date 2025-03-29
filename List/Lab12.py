# Create the List using the Range Function

#  -7  -6  -5  -4  -3  -2  -1  = -Ve Index
#[ 10, 20, 30, 40, 50, 60, 70 ]
#  0,  1,   2,  3,  4,  5,  6   = +Ve Index


mylist=[ 10, 20, 30, 40, 50, 60, 70 ]
length=len(mylist)
print(length)

print("----------------------")

print(list(range(length)))

print("----------------------")
for l in range(length):
    print(mylist[l])
