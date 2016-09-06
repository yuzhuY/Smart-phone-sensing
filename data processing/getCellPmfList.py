from readDataToList import readDataToList
from curveFit import gaussFit
from constants import *

def getCellPmfList(filePath, bestApList):
	
	dataList = readDataToList(filePath)

	rssiList = []
	for i in range(0, WIFINUM):
		rssiList.append([])

	for i in range(0, WIFINUM):
		for j in range(0, len(dataList)):
			if dataList[j] == bestApList[i]:
				rssiList[i].append(dataList[j + 1])

	### initial list
	cellPmfList = []
	for i in range(0, WIFINUM):
		cellPmfList.append([])
		for j in range(0 ,256):
			cellPmfList[i].append(0)

	### Step 1: Count the number
	for i in range(0, WIFINUM):
		if len(rssiList[i]) is not 0:
			for item in rssiList[i]:
				cellPmfList[i][int(-item)] = cellPmfList[i][int(-item)] + 1

	### Step 2: Gaussian fitting
	#gaussFit(cellPmfList)

	### Step 3: Calculate the pmf
	he = 0
	for row in cellPmfList:
		he = sum(row)
		if he != 0 :
			for i in range(0, len(row)):
				row[i] = row[i]*1.0/he

	return cellPmfList