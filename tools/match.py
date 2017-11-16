import numpy as np
from res import *

def hisen(array_):                                                                 
	array_ = np.array(array_)                                                                                                                      
	y,x = np.nonzero(array_) 
	# split array into x,y pairing list                                                                             
	for i in range(len(y)):                                                                                
	    y[i] = abs(40-y[i])  
	# convert into conventional coordination 
	return (x.tolist(),y.tolist())
# hisen's procedure                                                                                                                                                  

def text_match(mapping):
	for Ai,Bi in enumerate(mapping):
	    print("Point A[%d] goes to point B[%d]."%(Ai+1,Bi+1))

def minWithID(lst):
	val = min(lst)
	return (val, lst.index(val))

def all_match(M):
	used = [ False ] * len(M[0])
	# initialize used mark
	mapping = [ 0 ] * len(used)
	# mapping[i] = j => Ai => Bj
	MIN=0
	for Ai, arow in enumerate(M):
		min_val = 10000000
		min_i = -1
		# minmum index

		for i, val in enumerate(arow):
			if val < min_val and not used[i]:
				min_val = val
				min_i = i

		used[min_i] = True
		MIN += min_val
		mapping[Ai] = min_i
	return mapping

def max_distance(pairs):
	MAX=(0,)
	for i,j in pairs:
		if i > MAX[0]:
			MAX = (i,j)
	return MAX
	
def main(mat_A,mat_B):

	xa,ya = hisen(mat_A)                                                                                                                                                                                                                                    
	xb,yb = hisen(mat_B)  
	# Get pairs from A and B 

	A,B =zip(xa,ya),zip(xb,yb)
	# zip x,y into (x,y) coordination pairs

	M = [[((xb-xa)**2+(yb-ya)**2)**0.5 for xb, yb in B ] for xa, ya in A]
	# Calcute distance matrix M. The result in available at doc/distance_matrix.txt

	mapping = all_match(M)
	# get mapping table.
	pairs=list(map(lambda t: (t[0], t[1].index(t[0])), [(min(row),row) for row in M ]))
	# print tuples that contains minimum distance and index.
	print('\nMatch table:')
	text_match(mapping)
	# The result in available at doc/match_table.txt
	print('Max (distance,point_in_B) to move:'+str(max_distance(pairs)))
	

if __name__ == '__main__':
	main(fw,dg)
	main(dg,bl)
