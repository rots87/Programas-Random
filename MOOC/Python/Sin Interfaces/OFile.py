# Use words.txt as the file name
fname = input("Ingrese el nombre del archivo: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print (line)