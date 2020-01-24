#!/usr/bin/python3

def unique(data):
	out = []
	for each in data:
		if each not in out:
			out += [each]
	return out

def FormatData(FileName, year, TestSpecies):
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
			if i in [5, 9]: record += [each.replace('"',"")]
			i += 1
			
		if len(record) == 2 and record[0] != "" and record[1] != "":
			if str(year) in record[1] and record[0] == TestSpecies:
				species += [record[0]]
				date += [record[1]]
		else:
			errors += 1
			
	return species, date, errors

TestSpecies = input("enter species: ")
for each in range(1980, 2020):
	species, date, errors = FormatData("records-2019-11-07.csv", each, TestSpecies)
	print("{} | {}".format(each, len(species)))