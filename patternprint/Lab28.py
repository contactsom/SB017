'''
  A

         B B

        C C C

       D D D D

      E E E E E

     F F F F F F

    G G G G G G G

   H H H H H H H H

  I I I I I I I I I

 J J J J J J J J J J

'''

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),(chr(64+i)+" ")*i)
    print()