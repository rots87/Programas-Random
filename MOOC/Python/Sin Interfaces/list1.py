fname = input("Enter file name: ")
fh = open(fname)
words = list()
lst = list()
for line in fh:
    line = line.split()
    for i in line:
        if i not in lst:
            lst.append(i)
lst.sort()
print (lst)