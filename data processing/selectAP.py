from sortAp import sortAp
from apRank import apRank
from createTopAp import createTopAp
from readDataToList import readDataToList
from getCellPmfList import getCellPmfList
from cellToAp import cellToAp
from constants import *


#apRank1 = sortAp("./wifidata1")
#apRank2 = sortAp("./wifidata2")
#apRank3 = sortAp("./wifidata3")
#apRank4 = sortAp("./wifidata4")
#apRank5 = sortAp("./wifidata5")
#apRank6 = sortAp("./wifidata6")
#apRank7 = sortAp("./wifidata7")
#apRank8 = sortAp("./wifidata8")
#apRank9 = sortAp("./wifidata9")
#apRank10 = sortAp("./wifidata10")
#apRank11 = sortAp("./wifidata11")
#apRank12 = sortAp("./wifidata12")
#apRank13 = sortAp("./wifidata13")
#apRank14 = sortAp("./wifidata14")
#apRank15 = sortAp("./wifidata15")
apRank16 = sortAp("./16wifidata")
apRank17 = sortAp("./17wifidata")
apRank18 = sortAp("./18wifidata")


finalApRankDic = {}
#apRank(apRank1, finalApRankDic)
#apRank(apRank2, finalApRankDic)
#apRank(apRank3, finalApRankDic)
#apRank(apRank4, finalApRankDic)
#apRank(apRank5, finalApRankDic)
#apRank(apRank6, finalApRankDic)
#apRank(apRank7, finalApRankDic)
#apRank(apRank8, finalApRankDic)
#apRank(apRank9, finalApRankDic)
#apRank(apRank10, finalApRankDic)
#apRank(apRank11, finalApRankDic)
#apRank(apRank12, finalApRankDic)
#apRank(apRank13, finalApRankDic)
#apRank(apRank14, finalApRankDic)
#apRank(apRank15, finalApRankDic)
apRank(apRank16, finalApRankDic)
apRank(apRank17, finalApRankDic)
apRank(apRank18, finalApRankDic)


bestApList = []
createTopAp(finalApRankDic, bestApList)

#cellPmfList1 = getCellPmfList('./wifidata1', bestApList)
#cellPmfList2 = getCellPmfList('./wifidata2', bestApList)
#cellPmfList3 = getCellPmfList('./wifidata3', bestApList)
#cellPmfList4 = getCellPmfList('./wifidata4', bestApList)
#cellPmfList5 = getCellPmfList('./wifidata5', bestApList)
#cellPmfList6 = getCellPmfList('./wifidata6', bestApList)
#cellPmfList7 = getCellPmfList('./wifidata7', bestApList)
#cellPmfList8 = getCellPmfList('./wifidata8', bestApList)
#cellPmfList9 = getCellPmfList('./wifidata9', bestApList)
#cellPmfList10 = getCellPmfList('./wifidata10', bestApList)
#cellPmfList11 = getCellPmfList('./wifidata11', bestApList)
#cellPmfList12 = getCellPmfList('./wifidata12', bestApList)
#cellPmfList13 = getCellPmfList('./wifidata13', bestApList)
#cellPmfList14 = getCellPmfList('./wifidata14', bestApList)
#cellPmfList15 = getCellPmfList('./wifidata15', bestApList)
cellPmfList16 = getCellPmfList('./16wifidata', bestApList)
cellPmfList17 = getCellPmfList('./17wifidata', bestApList)
cellPmfList18 = getCellPmfList('./18wifidata', bestApList)


#cellPmfList = [cellPmfList1, cellPmfList2, cellPmfList3,
#			   cellPmfList4, cellPmfList5, cellPmfList6,
#			   cellPmfList7, cellPmfList8, cellPmfList9,
#			   cellPmfList10, cellPmfList11, cellPmfList12,
#			   cellPmfList13, cellPmfList14, cellPmfList15,
#			   cellPmfList16, cellPmfList17, cellPmfList18]
cellPmfList = [cellPmfList16, cellPmfList17, cellPmfList18]


for k in range(0, WIFINUM):
	fileName = 'ApPmf' + str(k) + '.csv'
	with open(fileName, 'w') as file:
		for i in range(0, CELLNUM):
			for j in range(0, 256):
				if j != 255:
					file.write(str(cellPmfList[i][k][j]) + ',')
				else:
					file.write(str(cellPmfList[i][k][j]) + '\n')

