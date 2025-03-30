file=open("simple.txt",'w')
print("File Name ::", file.name)
print("File Mode ::", file.mode)

print("File Readable ::", file.readable())
print("File Writable ::", file.writable())

print("Is File Open ::", file.closed)
file.close()
print("Is File Open ::", file.closed)




