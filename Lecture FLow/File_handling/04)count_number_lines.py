f=open("myfile.txt","r")

#print(f.read())
#print(f.readlines())

count=0

for row in f.readlines():
    print(row)
    count+=1

print(count)    
