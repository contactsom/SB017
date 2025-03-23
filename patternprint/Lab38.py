'''
            A
         C C C
        E E E E E
       G G G G G G G
      I I I I I I I I I
     K K K K K K K K K K K
    M M M M M M M M M M M M M
   O O O O O O O O O O O O O O O
  Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q
 S S S S S S S S S S S S S S S S S S S
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),(str(chr(64+2*i-1)+" "))*(2*i-1))