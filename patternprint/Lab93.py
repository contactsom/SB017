'''
E       E
 D     D
  C   C
   B B
    A 
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(i,i+1):
        print(chr(64+num-i+1),end=" ")
    if i<=4:
        print(" "*(2*num-2*i-2),end="")
        for k in range(i,i+1):
            print(chr(64+num-i+1),end=" ")
    print()