# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,'r')

for lx in fh:
	nl = lx.rstrip()
	print(nl.upper())
