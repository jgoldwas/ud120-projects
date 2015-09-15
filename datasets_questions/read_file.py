f = open('../final_project/poi_names.txt', 'r')

d = f.readline()
num_of_names = 0

while d != "":
	if d[0] == "(":
		num_of_names += 1
	d = f.readline()

print num_of_names

f.close()