import os

def sortAp(filePath):
	
	fileData = file(filePath)

	rowData = []

	for line in fileData:
		### Delete the line break in every row
		data, lineBreak = line.split('\n')

		### Delete the name of the AP
		temp = data.split(',')
		i = len(temp)/3
		for j in range(0, i):
			temp.pop(2*j)

		### Convert the RSS value to number
		for j in range(0, len(temp)):
			if j%2 is 1:
				temp[j] = float(temp[j])

		rowData.extend(temp)

	fileData.close()

	### Count the number of each AP appears in the rowData
	apAppearNum = {}
	for item in rowData:
		if isinstance(item, basestring):
			if item not in apAppearNum:
				apAppearNum[item] = rowData.count(item)
	sortedApNum = sorted(apAppearNum.items(), lambda x, y: cmp(x[1], y[1]), reverse=True) ### This is a list, 
																						  ### not a dictionary
	apRank = []
	i = 0
	for item in sortedApNum:
		if i == 0:
			apRank.append((item[0], 10))
		elif i > 0 and i <= 5:
			apRank.append((item[0], 5))
		elif i > 5 and i <= 10:
			apRank.append((item[0], 2))
		elif i > 10 and i <= 20:
			apRank.append((item[0], 1))
			
		i = i + 1

	return apRank