game = [[1,1,1],[1,-1,-1],[1,1,-1]]

def formatvalidator(g):
  	if isinstance(g, list):
		if len(g) == 3:
	  		if len(g[0]) == 3 and len(g[1])==3 and len(g[2]) == 3:
				for i in g:
		  			for i2 in i:
						if isinstance(i2, int):
			  				if abs(i2) == 1 or i2 == 0:
								pass
			  				else:
								return False
						else:
			  				return False
				return True
	  		else:
				return False
		else:
	  		return False
  	else:
		return False


def rulevalidator(g):
	countx = 0
	counto = 0
	count0 = 0

	for i in g:
		for i2 in i:
			if i2 == 1:
				countx += 1
			elif i2 == -1:
				counto+= 1
			elif i2 == 0:
				count0 +=1

	if countx == counto:
		return 1
	elif countx == counto +1:
		return -1
	else:
		return False

def windiagonal(g):
	if g[1][1] != 0:
		if ((g[0][0] == g[1][1]) and (g[1][1]==g[2][2])) or ((g[0][2] == g[1][1]) and (g[1][1] == g[2][0])):
			return g[1][1]
		else:
			return False
	else:
		return False


def winhorizontal(g):
	for i in g:
		if i[0] != 0:
			if (i[0] == i[1]) and (i[1] == i[2]):
				return i[0]
	return False

print  rulevalidator(game)
