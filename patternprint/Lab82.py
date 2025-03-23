'''
    A
   A B
  A B C
 A B C D
A B C D E
 B C D E
  C D E
   D E
    E
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
for p in range(1,num):
    print(" "*p,end="")
    for q in range(1,num+1-p):
        print(chr(64+q+p),end=" ")
    print()