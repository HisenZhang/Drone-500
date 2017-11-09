from PIL import Image
import argparse
import numpy as np

# argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str, help='Input file path.')
parser.add_argument('--output', type=str, help='Output file path.')
parser.add_argument('h', type=int, help='Height.')
parser.add_argument('w', type=int, help='Width.')
args = parser.parse_args()

# img process

im = Image.open(args.input)
im = im.resize((args.h,args.w), Image.ANTIALIAS)	
# obj.resize((height,width),algorithm)
modified = im.convert('1')
array = np.array(modified)
# save as an array. For later use.
modified.show()

if args.output:
	modified.save(args.output ,format='png')
else:
	try:
		modified.save(str(hash(args.input))[:4]+'.png',format='png')
		pass
	except IOError:
		raise IOError

count_white,count_black = 0,0
# Initialize counter
for i in np.nditer(np.array(modified)):
	if i == False:
		count_white += 1
	else:
		count_black += 1
print("False %d,True %d, Total %d." % (count_white,count_black,count_black+count_white))
# statistic module

x,y=[],[]
# x stores x-coordinate, y for y-values

array = array.tolist()
for i in range(len(array)):
	for j in range(len(array[i])):
		array[i][j] = not array[i][j]
array = np.array(array)
# turn into list, take the not() value, then back to ndarray

y,x = np.nonzero(array)
for i in range(len(y)):
	y[i] = abs(args.w-y[i])
# convert into conventional coordinate

print('x = '+str(x))
print('y = '+str(y))
# output