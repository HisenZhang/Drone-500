from PIL import Image
import argparse
import numpy as np

# argparse
def args_picking():
	parser = argparse.ArgumentParser()
	parser.add_argument('input', type=str, help='Input file path.')
	parser.add_argument('h', type=int, help='Height.')
	parser.add_argument('w', type=int, help='Width.')
	parser.add_argument('--reverse', type=bool, help='Reverse 0 and 1 switch.')
	parser.add_argument('--output', type=str, help='Output file path.')
	args = parser.parse_args()
	return args

def image_save(args,modified):
	if args.output:
		modified.save(args.output ,format='png')
		# if output specified.
	else:
		try:
			modified.save(str(hash(args.input))[:4]+'.png',format='png')
			pass
		except IOError:
			raise IOError
	pass

def image_stat(matrix):
	count_white,count_black = 0,0
	# Initialize counter
	for i in np.nditer(np.array(matrix)):
		if i == False:
			count_white += 1
		else:
			count_black += 1
	print("False %d,True %d, Total %d.\n\n########" % (count_white,count_black,count_black+count_white))
	pass
	# statistic module

def image_rev(array):
	array = array.tolist()
	for i in range(len(array)):
		for j in range(len(array[i])):
			array[i][j] = not array[i][j]
	return np.array(array)
	# if reverse required, turn into list, take the not() value, then back to ndarray

def coordination_cvrt(args,array):
	y,x = np.nonzero(array)
	for i in range(len(y)):
		y[i] = abs(args.h-y[i])
	# convert into conventional coordinate
	return y,x

def curve_range(x,y):
	x.sort(reverse=True)
	y.sort(reverse=True)
	# sort to get minimum and maximum.
	print('Range X Min: %d,Max: %d' % (x[len(x)-1],x[0]))
	print('Range Y Min: %d,Max: %d' % (y[len(y)-1],y[0]))
	# output
	pass

def main():
	# img process
	args = args_picking()
	modified = (((Image.open(args.input)).resize((args.h,args.w), Image.ANTIALIAS)).convert('1'))
	array = np.array(modified)
	# obj.resize((height,width),algorithm)
	# save as an array. For later use.
	modified.show()

	image_save(args,modified)
	image_stat(modified)

	if args.reverse:
		array = image_rev(array)

	y,x = coordination_cvrt(args,array)
	x,y = x.tolist(),y.tolist()

	print('x = '+str(x)+'\ny = '+str(y)+'\n\n########')
	# output of x,y pairs
	curve_range(x,y)
	pass

if __name__ == '__main__':
	main()