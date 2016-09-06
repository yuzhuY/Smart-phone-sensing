from constants import *

def cellToAp(cellPmfList):
	
	#initial the list
	apPmfList = []
	for i in range(0, WIFINUM):
		apPmfList.append([])
		for j in range(0, CELLNUM):
			apPmfList[i].append(cellPmfList[j][i])

	return apPmfList
