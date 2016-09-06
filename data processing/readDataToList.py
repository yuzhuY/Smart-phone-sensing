###################################################################################
# get the path of the data file, delete the AP name and line break, 
# convert the RSS string value to number, return the list 
###################################################################################
def readDataToList(filePath):

	dataList = []

	fileData = file(filePath)

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

		dataList.extend(temp)

	fileData.close()

	return dataList

