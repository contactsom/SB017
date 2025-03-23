'''
 10 10 10 10 10 10 10 10 10 10
  9 9 9 9 9 9 9 9 9
   8 8 8 8 8 8 8 8
    7 7 7 7 7 7 7
     6 6 6 6 6 6
      5 5 5 5 5
       4 4 4 4
        3 3 3
         2 2
          1
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),(str(n+1-i)+" ")*(n+1-i))