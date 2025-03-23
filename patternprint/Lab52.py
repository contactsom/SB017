'''
E E E E E E E E E
 D D D D D D D
  C C C C C
   B B B
    A 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(chr(65+num-i),end=" ")
    for k in range(2,num+2-i):
        print(chr(65+num-i),end=" ")
    print()