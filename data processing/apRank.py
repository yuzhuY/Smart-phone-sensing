def apRank(apList, apDic):

	for item in apList:
		if item[0] in apDic:
			apDic[item[0]] = apDic[item[0]] + item[1]
		else:
			apDic[item[0]] = item[1]

