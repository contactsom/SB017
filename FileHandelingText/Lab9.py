file=open("Simplilearn.txt",'r') # Read
lines=file.readlines()

for line in lines:
    print(line)


file.close()




