file = open("read_file","r")
cnt = 0
for line in file:	 
	cnt += 1
	print("Line {}: {}".format((cnt),(line)))
