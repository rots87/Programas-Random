fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
lst = list()
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From"): continue
    if line.startswith('From:'): continue
    line = line.split()
    words = line[1]
    lst.append(words)
    count = count + 1

for elements in lst:
    print (elements)

print ("There were" , count , "lines in the file with From as the first word")