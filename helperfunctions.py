def countZeroes(tmpHash):
	cnt = 0
	for i in tmpHash:
		if i != '0':
			break
		cnt += 1
	return cnt