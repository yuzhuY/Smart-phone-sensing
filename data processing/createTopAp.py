###########################################################################
### Sort the fianlApRank first, then pass the mac address 
### of the top 30 AP to the list bestAp.
### Also create a file named topAp to store the top 30 AP.
###########################################################################
from constants import *
def createTopAp(finalApRankDic, bestApList):

	### Sort the AP to a list
	apRankList = sorted(finalApRankDic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

	### 30 best AP
	file = open('topAp', 'w')
	for i in range(0, WIFINUM):
		file.write(apRankList[i][0] + '\n')
		bestApList.append(apRankList[i][0])

	file.close()