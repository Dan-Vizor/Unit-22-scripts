#!/usr/bin/python3

def unique(data):
	out = []
	for each in data:
		if each not in out:
			out += [each]
	return out

def FormatData(FileName):
	file = open(FileName, "r")

	species = []
	date = []
	errors = 0
	for line in file:
		if "NBN Atlas record ID" in line: continue
		line = line.split(",")
		
		record = []
		i = 0
		for each in line:
			if i in [7, 11]: record += [each.replace('"',"")]
			i += 1
			
		if len(record) == 2 and record[0] != "" and record[1] != "":
			species += [record[0]]
			date += [record[1]]
		else:
			errors += 1
			
	return species, date, errors

species, date, errors = FormatData("Tewkesbury_data.csv")
for each in unique(species):
	print(each + " | " + str(species.count(each)))
print("\n{} invalid records".format(errors))
