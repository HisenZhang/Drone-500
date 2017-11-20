def dfs(u):
	checkx[u]=1
	for i in range(0,n): 
		if(zx[u]+zy[i]==W[u][i] and not check[i]):
			check[i]=1
			if(macy[i]== -1 or dfs(macy[i])):
				macy[i]=u
				return 1
		if(not check[i]):
			Y1[i]=min(Y1[i],zx[u]+zy[i]-W[u][i])
	return 0

def gx():
	global INF
	a = INF

	for i in range(0,n):
		if(not check[i]):
			a = min(a,Y1[i])

	for i in range(0,n):
		if(check[i]): 
			zy[i]+=a
		if(checkx[i]): 
			zx[i]-=a
	
def xyl():
	global macy
	global check
	global checkx

	macy = [ -1 ] * N
	i = 0
	while i < n:
		check = [ 0 ] * N
		checkx = [ 0 ] * N
		if (not dfs(i)):
			i-=1
			gx()
		i += 1
		
def main():
	global macy,INF
	for i in range(N):
		zx[i] = -INF
		for j in range(N):
			M[i][j] *= -1
			zx[i] = max(zx[i], M[i][j])
			Y1[j] = INF

	xyl()
	
	p = 0
	for i in range(0,n):
		u = macy[i]
		p += W[u][i]

	print(macy)
	print(-p)

if __name__ == '__main__':
	with open("M.txt") as fp:
		M = eval(fp.read())
	INF = float("inf")
	N = len(M)
	W = M
	X,Y = [ 0 ] * N,[ 0 ] * N
	macy = [ 0 ] * N
	check = [ False ] * N
	checkx = [ False ] * N
	zx = [ 0 ] * N
	zy = [ 0 ] * N
	Y1 = [ 0 ] * N
	n = N
	main()