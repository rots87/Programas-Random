# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
average = 0
count = 0
Sum = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    value = line[20:]
    Sum = Sum + float(value)
    count = count + 1
average = Sum / count
print ("Average spam confidence:", average)
