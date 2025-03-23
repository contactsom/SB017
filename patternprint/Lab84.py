'''
     5
   5 4 5
  5 4 3 4 5
 5 4 3 2 3 4 5
5 4 3 2 1 2 3 4 5
 5 4 3 2 3 4 5
  5 4 3 4 5
   5 4 5
    5
'''
while True:
    n=int(input("Enter a number:"))
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print(n+1-j,end=" ")
        for k in range(2,i+1):
            print(n-i+k,end=" ")
        print()
    for i in range(1,n+1):
        print(" "*i,end="")
        for j in range(1,n+1-i):
            print(n+1-j,end=" ")
        for k in range(2,n+1-i):
            print(i+k,end=" ")
        print()