'''
E
E D
E D C
E D C B
E D C B A
E D C B
E D C
E D
E
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(65+num-j),end=" ")
    print()
for a in range(1,num+1):
    for k in range(num-a,0,-1):
        print(chr(64+k+a),end=" ")
    print()
