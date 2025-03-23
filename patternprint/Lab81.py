'''
    A
   B B
  C C C
 D D D D
E E E E E
 D D D D
  C C C
   B B
    A 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
for p in range(1,num):
    print(" "*p,end="")
    for q in range(1,num+1-p):
        print(chr(64+num-p),end=" ")
    print()