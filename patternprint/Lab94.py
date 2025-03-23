'''
A       A
 B     B
  C   C
   D D
    E 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(i,i+1):
        print(chr(64+i),end=" ")
    if i<=4:
        print(" " * (2 * num - 2 * i - 2), end="")
        for k in range(i, i + 1):
            print(chr(64 + i), end=" ")
    print()