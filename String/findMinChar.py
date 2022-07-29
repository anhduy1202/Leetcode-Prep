def findMinChar(searchWord,resultWord):
	p, q = 0, 0
	while p < len(searchWord):
		if searchWord[p] == resultWord[q]:
			q += 1
			if q == len(resultWord):
				return 0
		p += 1
	return len(resultWord) - q

print(findMinChar("armaze","amazon"))