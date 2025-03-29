# Create the List using the Range Function

#  -7  -6  -5  -4  -3  -2  -1  = -Ve Index
#[ 10, 20, 30, 40, 50, 60, 70 ]
#  0,  1,   2,  3,  4,  5,  6   = +Ve Index


mylist=[ 10, 20, 30, 40, 50, 60, 70 ]
print(mylist)
print(type(mylist))

print("----------------------------")

print("From Index 1 to Index 3 -- ",mylist[1:3]) #  [20, 30]
print("From Index -5 to Index -2 -- ",mylist[-5:-2]) #[30, 40, 50]

