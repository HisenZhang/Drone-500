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

im=Image.open(args.input)
im = im.resize((args.h,args.w), Image.ANTIALIAS)	
# obj.resize((height,width),algorithm)
modified=im.convert('1')
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