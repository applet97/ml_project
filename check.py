def loadData(filename):
	file = open(filename).readlines()
	trainingSet = []
	for i in range(len(file)):
		trainingSet.append(file[i].strip().split(','))
	return trainingSet

def main():
	trainingSet = loadData('car.data')
	Vocabulary = len(trainingSet)
	trainingSetUnAcc = []
	trainingSetAcc = []
	trainingSetGood = []
	trainingSetVgood = []
	UnAccCase = []
	AccCase = []
	GoodCase = []
	VgoodCase = []
	 
	for i in range(len(trainingSet)):
		if trainingSet[i][-1] == 'unacc':
			trainingSetUnAcc.append(trainingSet[i])
		elif trainingSet[i][-1] == 'acc':
			trainingSetAcc.append(trainingSet[i])
		elif trainingSet[i][-1] == 'good':
			trainingSetGood.append(trainingSet[i])
		elif trainingSet[i][-1] == 'vgood':
			trainingSetVgood.append(trainingSet[i])

	ProbabilityOfClassUnAcc = len(trainingSetUnAcc)/Vocabulary
	ProbabilityOfClassAcc = len(trainingSetAcc)/Vocabulary
	ProbabilityOfClassGood = len(trainingSetGood)/Vocabulary
	ProbabilityOfClassVgood = len(trainingSetVgood)/Vocabulary

	bVhigh = bHigh = bMed = bLow = mVhigh = mHigh = mMed = mLow = d2 = d3 = d4 = d5more = p2 = p4 = pMore = lgSmall = lgMed = lgBig = sLow = sMed = sHigh = 0 
	for i in range(len(trainingSetUnAcc)):
		for j in range(6):
			if j == 0:
				if trainingSetUnAcc[i][j] == "vhigh":
					bVhigh+=1
				elif trainingSetUnAcc[i][j] == "high":
					bHigh+=1
				elif trainingSetUnAcc[i][j] == "med":
					bMed+=1
				elif trainingSetUnAcc[i][j] == "low":
					bLow+=1
			elif j == 1:
				if trainingSetUnAcc[i][j] == "vhigh":
					mVhigh+=1
				elif trainingSetUnAcc[i][j] == "high":
					mHigh+=1
				elif trainingSetUnAcc[i][j] == "med":
					mMed+=1
				elif trainingSetUnAcc[i][j] == "low":
					mLow+=1
			elif j == 2:
				if trainingSetUnAcc[i][j] == "2":
					d2+=1
				elif trainingSetUnAcc[i][j] == "3":
					d3+=1
				elif trainingSetUnAcc[i][j] == "4":
					d4+=1
				elif trainingSetUnAcc[i][j] == "5more":
					d5more+=1
			elif j == 3:
				if trainingSetUnAcc[i][j] == "2":
					p2+=1
				elif trainingSetUnAcc[i][j] == "4":
					p4+=1
				elif trainingSetUnAcc[i][j] == "more":
					pMore+=1
			elif j == 4:
				if trainingSetUnAcc[i][j] == "small":
					lgSmall+=1
				elif trainingSetUnAcc[i][j] == "med":
					lgMed+=1
				elif trainingSetUnAcc[i][j] == "big":
					lgBig+=1
			elif j ==5:
				if trainingSetUnAcc[i][j] == "low":
					sLow+=1
				elif trainingSetUnAcc[i][j] == "med":
					sMed+=1
				elif trainingSetUnAcc[i][j] == "high":
					sHigh+=1
	toAppend = []
	toAppend.append(bVhigh)
	toAppend.append(bHigh)
	toAppend.append(bMed)
	toAppend.append(bLow)
	UnAccCase.append(toAppend)

	toAppend = []
	toAppend.append(mVhigh)
	toAppend.append(mHigh)
	toAppend.append(mMed)
	toAppend.append(mLow)
	UnAccCase.append(toAppend)

	toAppend = []
	toAppend.append(d2)
	toAppend.append(d3)
	toAppend.append(d4)
	toAppend.append(d5more)
	UnAccCase.append(toAppend)

	toAppend = []
	toAppend.append(p2)
	toAppend.append(p4)
	toAppend.append(pMore)
	UnAccCase.append(toAppend)

	toAppend = []
	toAppend.append(lgSmall)
	toAppend.append(lgMed)
	toAppend.append(lgBig)
	UnAccCase.append(toAppend)

	toAppend = []
	toAppend.append(sLow)
	toAppend.append(sMed)
	toAppend.append(sHigh)
	UnAccCase.append(toAppend)

	bVhigh = bHigh = bMed = bLow = mVhigh = mHigh = mMed = mLow = d2 = d3 = d4 = d5more = p2 = p4 = pMore = lgSmall = lgMed = lgBig = sLow = sMed = sHigh = 0 
	for i in range(len(trainingSetAcc)):
		for j in range(6):
			if j == 0:
				if trainingSetAcc[i][j] == "vhigh":
					bVhigh+=1
				elif trainingSetAcc[i][j] == "high":
					bHigh+=1
				elif trainingSetAcc[i][j] == "med":
					bMed+=1
				elif trainingSetAcc[i][j] == "low":
					bLow+=1
			elif j == 1:
				if trainingSetAcc[i][j] == "vhigh":
					mVhigh+=1
				elif trainingSetAcc[i][j] == "high":
					mHigh+=1
				elif trainingSetAcc[i][j] == "med":
					mMed+=1
				elif trainingSetAcc[i][j] == "low":
					mLow+=1
			elif j == 2:
				if trainingSetAcc[i][j] == "2":
					d2+=1
				elif trainingSetAcc[i][j] == "3":
					d3+=1
				elif trainingSetAcc[i][j] == "4":
					d4+=1
				elif trainingSetAcc[i][j] == "5more":
					d5more+=1
			elif j == 3:
				if trainingSetAcc[i][j] == "2":
					p2+=1
				elif trainingSetAcc[i][j] == "4":
					p4+=1
				elif trainingSetAcc[i][j] == "more":
					pMore+=1
			elif j == 4:
				if trainingSetAcc[i][j] == "small":
					lgSmall+=1
				elif trainingSetAcc[i][j] == "med":
					lgMed+=1
				elif trainingSetAcc[i][j] == "big":
					lgBig+=1
			elif j ==5:
				if trainingSetAcc[i][j] == "low":
					sLow+=1
				elif trainingSetAcc[i][j] == "med":
					sMed+=1
				elif trainingSetAcc[i][j] == "high":
					sHigh+=1
	toAppend = []
	toAppend.append(bVhigh)
	toAppend.append(bHigh)
	toAppend.append(bMed)
	toAppend.append(bLow)
	AccCase.append(toAppend)

	toAppend = []
	toAppend.append(mVhigh)
	toAppend.append(mHigh)
	toAppend.append(mMed)
	toAppend.append(mLow)
	AccCase.append(toAppend)

	toAppend = []
	toAppend.append(d2)
	toAppend.append(d3)
	toAppend.append(d4)
	toAppend.append(d5more)
	AccCase.append(toAppend)

	toAppend = []
	toAppend.append(p2)
	toAppend.append(p4)
	toAppend.append(pMore)
	AccCase.append(toAppend)

	toAppend = []
	toAppend.append(lgSmall)
	toAppend.append(lgMed)
	toAppend.append(lgBig)
	AccCase.append(toAppend)

	toAppend = []
	toAppend.append(sLow)
	toAppend.append(sMed)
	toAppend.append(sHigh)
	AccCase.append(toAppend)

	bVhigh = bHigh = bMed = bLow = mVhigh = mHigh = mMed = mLow = d2 = d3 = d4 = d5more = p2 = p4 = pMore = lgSmall = lgMed = lgBig = sLow = sMed = sHigh = 0 
	for i in range(len(trainingSetGood)):
		for j in range(6):
			if j == 0:
				if trainingSetGood[i][j] == "vhigh":
					bVhigh+=1
				elif trainingSetGood[i][j] == "high":
					bHigh+=1
				elif trainingSetGood[i][j] == "med":
					bMed+=1
				elif trainingSetGood[i][j] == "low":
					bLow+=1
			elif j == 1:
				if trainingSetGood[i][j] == "vhigh":
					mVhigh+=1
				elif trainingSetGood[i][j] == "high":
					mHigh+=1
				elif trainingSetGood[i][j] == "med":
					mMed+=1
				elif trainingSetGood[i][j] == "low":
					mLow+=1
			elif j == 2:
				if trainingSetGood[i][j] == "2":
					d2+=1
				elif trainingSetGood[i][j] == "3":
					d3+=1
				elif trainingSetGood[i][j] == "4":
					d4+=1
				elif trainingSetGood[i][j] == "5more":
					d5more+=1
			elif j == 3:
				if trainingSetGood[i][j] == "2":
					p2+=1
				elif trainingSetGood[i][j] == "4":
					p4+=1
				elif trainingSetGood[i][j] == "more":
					pMore+=1
			elif j == 4:
				if trainingSetGood[i][j] == "small":
					lgSmall+=1
				elif trainingSetGood[i][j] == "med":
					lgMed+=1
				elif trainingSetGood[i][j] == "big":
					lgBig+=1
			elif j ==5:
				if trainingSetGood[i][j] == "low":
					sLow+=1
				elif trainingSetGood[i][j] == "med":
					sMed+=1
				elif trainingSetGood[i][j] == "high":
					sHigh+=1
	toAppend = []
	toAppend.append(bVhigh)
	toAppend.append(bHigh)
	toAppend.append(bMed)
	toAppend.append(bLow)
	GoodCase.append(toAppend)

	toAppend = []
	toAppend.append(mVhigh)
	toAppend.append(mHigh)
	toAppend.append(mMed)
	toAppend.append(mLow)
	GoodCase.append(toAppend)

	toAppend = []
	toAppend.append(d2)
	toAppend.append(d3)
	toAppend.append(d4)
	toAppend.append(d5more)
	GoodCase.append(toAppend)

	toAppend = []
	toAppend.append(p2)
	toAppend.append(p4)
	toAppend.append(pMore)
	GoodCase.append(toAppend)

	toAppend = []
	toAppend.append(lgSmall)
	toAppend.append(lgMed)
	toAppend.append(lgBig)
	GoodCase.append(toAppend)

	toAppend = []
	toAppend.append(sLow)
	toAppend.append(sMed)
	toAppend.append(sHigh)
	GoodCase.append(toAppend)

	bVhigh = bHigh = bMed = bLow = mVhigh = mHigh = mMed = mLow = d2 = d3 = d4 = d5more = p2 = p4 = pMore = lgSmall = lgMed = lgBig = sLow = sMed = sHigh = 0 
	for i in range(len(trainingSetVgood)):
		for j in range(6):
			if j == 0:
				if trainingSetVgood[i][j] == "vhigh":
					bVhigh+=1
				elif trainingSetVgood[i][j] == "high":
					bHigh+=1
				elif trainingSetVgood[i][j] == "med":
					bMed+=1
				elif trainingSetVgood[i][j] == "low":
					bLow+=1
			elif j == 1:
				if trainingSetVgood[i][j] == "vhigh":
					mVhigh+=1
				elif trainingSetVgood[i][j] == "high":
					mHigh+=1
				elif trainingSetVgood[i][j] == "med":
					mMed+=1
				elif trainingSetVgood[i][j] == "low":
					mLow+=1
			elif j == 2:
				if trainingSetVgood[i][j] == "2":
					d2+=1
				elif trainingSetVgood[i][j] == "3":
					d3+=1
				elif trainingSetVgood[i][j] == "4":
					d4+=1
				elif trainingSetVgood[i][j] == "5more":
					d5more+=1
			elif j == 3:
				if trainingSetVgood[i][j] == "2":
					p2+=1
				elif trainingSetVgood[i][j] == "4":
					p4+=1
				elif trainingSetVgood[i][j] == "more":
					pMore+=1
			elif j == 4:
				if trainingSetVgood[i][j] == "small":
					lgSmall+=1
				elif trainingSetVgood[i][j] == "med":
					lgMed+=1
				elif trainingSetVgood[i][j] == "big":
					lgBig+=1
			elif j ==5:
				if trainingSetVgood[i][j] == "low":
					sLow+=1
				elif trainingSetVgood[i][j] == "med":
					sMed+=1
				elif trainingSetVgood[i][j] == "high":
					sHigh+=1
	toAppend = []
	toAppend.append(bVhigh)
	toAppend.append(bHigh)
	toAppend.append(bMed)
	toAppend.append(bLow)
	VgoodCase.append(toAppend)

	toAppend = []
	toAppend.append(mVhigh)
	toAppend.append(mHigh)
	toAppend.append(mMed)
	toAppend.append(mLow)
	VgoodCase.append(toAppend)

	toAppend = []
	toAppend.append(d2)
	toAppend.append(d3)
	toAppend.append(d4)
	toAppend.append(d5more)
	VgoodCase.append(toAppend)

	toAppend = []
	toAppend.append(p2)
	toAppend.append(p4)
	toAppend.append(pMore)
	VgoodCase.append(toAppend)

	toAppend = []
	toAppend.append(lgSmall)
	toAppend.append(lgMed)
	toAppend.append(lgBig)
	VgoodCase.append(toAppend)

	toAppend = []
	toAppend.append(sLow)
	toAppend.append(sMed)
	toAppend.append(sHigh)
	VgoodCase.append(toAppend)

	UnaccProb = []
	AccProb = []
	GoodProb = []
	VgoodProb = []

	testSet = input("Enter test set\n")
	testSet = testSet.split()

	for i in range(len(testSet)):
		if i == 0:
			if testSet[i] == "vhigh":
				UnaccProb.append((UnAccCase[i][0]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][0]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][0]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][0]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "high":
				UnaccProb.append((UnAccCase[i][1]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][1]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][1]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][1]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "med":
				UnaccProb.append((UnAccCase[i][2]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][2]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][2]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][2]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "low":
				UnaccProb.append((UnAccCase[i][3]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][3]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][3]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][3]+1)/(Vocabulary+len(trainingSetVgood)))
		elif i == 1:
			if testSet[i] == "vhigh":
				UnaccProb.append((UnAccCase[i][0]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][0]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][0]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][0]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "high":
				UnaccProb.append((UnAccCase[i][1]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][1]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][1]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][1]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "med":
				UnaccProb.append((UnAccCase[i][2]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][2]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][2]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][2]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "low":
				UnaccProb.append((UnAccCase[i][3]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][3]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][3]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][3]+1)/(Vocabulary+len(trainingSetVgood)))
		elif i == 2:
			if testSet[i] == "2":
				UnaccProb.append((UnAccCase[i][0]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][0]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][0]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][0]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "3":
				UnaccProb.append((UnAccCase[i][1]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][1]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][1]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][1]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "4":
				UnaccProb.append((UnAccCase[i][2]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][2]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][2]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][2]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "5more":
				UnaccProb.append((UnAccCase[i][3]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][3]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][3]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][3]+1)/(Vocabulary+len(trainingSetVgood)))
		elif i == 3:
			if testSet[i] == "2":
				UnaccProb.append((UnAccCase[i][0]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][0]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][0]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][0]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "4":
				UnaccProb.append((UnAccCase[i][1]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][1]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][1]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][1]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "more":
				UnaccProb.append((UnAccCase[i][2]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][2]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][2]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][2]+1)/(Vocabulary+len(trainingSetVgood)))
		elif i == 4:
			if testSet[i] == "small":
				UnaccProb.append((UnAccCase[i][0]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][0]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][0]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][0]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "med":
				UnaccProb.append((UnAccCase[i][1]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][1]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][1]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][1]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "big":
				UnaccProb.append((UnAccCase[i][2]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][2]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][2]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][2]+1)/(Vocabulary+len(trainingSetVgood)))
		elif i == 5:
			if testSet[i] == "low":
				UnaccProb.append((UnAccCase[i][0]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][0]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][0]+1/(Vocabulary+len(trainingSetGood))))
				VgoodProb.append((VgoodCase[i][0]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "med":
				UnaccProb.append((UnAccCase[i][1]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][1]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][1]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][1]+1)/(Vocabulary+len(trainingSetVgood)))
			elif testSet[i] == "high":
				UnaccProb.append((UnAccCase[i][2]+1)/(Vocabulary+len(trainingSetUnAcc)))
				AccProb.append((AccCase[i][2]+1)/(Vocabulary+len(trainingSetAcc)))
				GoodProb.append((GoodCase[i][2]+1)/(Vocabulary+len(trainingSetGood)))
				VgoodProb.append((VgoodCase[i][2]+1)/(Vocabulary+len(trainingSetVgood)))

	for i in range(len(testSet)):
		ProbabilityOfClassUnAcc*=UnaccProb[i]
		ProbabilityOfClassAcc*=AccProb[i]
		ProbabilityOfClassGood*=GoodProb[i]
		ProbabilityOfClassVgood*=VgoodProb[i]

	ProbabilityOfClassUnAcc/=(ProbabilityOfClassUnAcc+ProbabilityOfClassAcc+ProbabilityOfClassGood+ProbabilityOfClassVgood)
	ProbabilityOfClassAcc/=(ProbabilityOfClassUnAcc+ProbabilityOfClassAcc+ProbabilityOfClassGood+ProbabilityOfClassVgood)
	ProbabilityOfClassGood/=(ProbabilityOfClassUnAcc+ProbabilityOfClassAcc+ProbabilityOfClassGood+ProbabilityOfClassVgood)
	ProbabilityOfClassVgood/=(ProbabilityOfClassUnAcc+ProbabilityOfClassAcc+ProbabilityOfClassGood+ProbabilityOfClassVgood)

	print(ProbabilityOfClassUnAcc)
	print(ProbabilityOfClassAcc)
	print(ProbabilityOfClassGood)
	print(ProbabilityOfClassVgood)

	if ProbabilityOfClassUnAcc > ProbabilityOfClassAcc and ProbabilityOfClassUnAcc > ProbabilityOfClassGood and ProbabilityOfClassUnAcc > ProbabilityOfClassVgood:
		print("Unacc")
	elif ProbabilityOfClassAcc > ProbabilityOfClassUnAcc and ProbabilityOfClassAcc > ProbabilityOfClassGood and ProbabilityOfClassAcc > ProbabilityOfClassVgood:
		print("Acc")
	elif ProbabilityOfClassGood > ProbabilityOfClassUnAcc and ProbabilityOfClassGood > ProbabilityOfClassAcc and ProbabilityOfClassGood > ProbabilityOfClassVgood:
		print("Good")
	elif ProbabilityOfClassVgood > ProbabilityOfClassUnAcc and ProbabilityOfClassVgood > ProbabilityOfClassAcc and ProbabilityOfClassVgood > ProbabilityOfClassGood:
		print("Vgood")
main()