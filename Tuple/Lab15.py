#   -7  -6  -5  -4  -3  -2  -1  = -Ve Index
# ( 10, 20, 30, 40, 50, 60, 70 )
#   0,  1,   2,  3,  4,  5,  6   = +Ve Index

myTuple=( 10, 20, 30, 40, 50, 60, 70 )
print("[2,5]",myTuple[2:5]) # (30, 40, 50)
print("[2,5]",myTuple[2:50000]) # (30, 40, 50, 60, 70)
print("[2,5]",myTuple[2:]) #(30, 40, 50, 60, 70)
print("[2,5]",myTuple[:5]) # (10, 20, 30, 40, 50)

print("----------------------------------")
print("[-2,-5]",myTuple[-2:-5]) # ()
print("[-2,-5]",myTuple[-2:5]) # ()
print("[-2,-5]",myTuple[-5:-2]) # (30, 40, 50)



