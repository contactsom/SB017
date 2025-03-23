'''
          1
        1 2 3
       1 2 3 4 5
      1 2 3 4 5 6 7
     1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9 10 11
   1 2 3 4 5 6 7 8 9 10 11 12 13
  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(j,end=" ")
    print()