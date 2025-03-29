#   -7  -6  -5  -4  -3  -2  -1  = -Ve Index
# ( 10, 20, 30, 40, 50, 60, 70 )
#   0,  1,   2,  3,  4,  5,  6   = +Ve Index

myTuple=( 10, 20, 30, 40, 50, 60, 70 )
print(myTuple[0]) # 10
myTuple[0]=100 # TypeError: 'tuple' object does not support item assignment

print(myTuple) #



