'''
E
D D
C C C
B B B B
A A A A A
B B B B
C C C
D D
E
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(65+num-i),end=" ")
    print()
for a in range(1,num+1):
    for k in range(0,num-a):
        print(chr(65+a),end=" ")
    print()