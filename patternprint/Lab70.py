'''
    A
   A B
  A B C
 A B C D
A B C D E 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,1+i):
        print(chr(64+j),end=" ")
    print()