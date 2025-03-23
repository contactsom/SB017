'''
A B C D E
 A B C D
  A B C
   A B
    A 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(chr(64+j),end=" ")
    print()