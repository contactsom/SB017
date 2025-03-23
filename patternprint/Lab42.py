'''
          A
        C B A
       E D C B A
      G F E D C B A
     I H G F E D C B A
    K J I H G F E D C B A
   M L K J I H G F E D C B A
  O N M L K J I H G F E D C B A
 Q P O N M L K J I H G F E D C B A
S R Q P O N M L K J I H G F E D C B A
'''
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(65+2*i-2,64,-1):
        print(chr(j),end=" ")
    print()