# Drone 500

This repository contains files for Drone 500 Project.

## File


```
.
├── doc		// documentation & text files
├── img		// images used
│   ├── matrix	// processed images
│   ├── raw	// raw images
│   └── separated	// the curves
├── map		// maps in .pdf
├── mat		// matrix in .mat and .xlsx
└── tools	// contains several ulitilies
```

## Utility

### resize

```
usage: resize.py [-h] [--reverse REVERSE] [--output OUTPUT] input h w

positional arguments:
  input              Input file path.
  h                  Height.
  w                  Width.

optional arguments:
  -h, --help         show this help message and exit
  --reverse REVERSE  Reverse 0 and 1 switch
  --output OUTPUT    Output file path.
```

This program basically functions in following pattern:

1. Resize the picture into the geometry given;
2. Convert to 0-1 matrix and save.
3. Get indexes of '1' elements.
4. Convert into conventional coordinate system as output.

For more information please view [documentation](./doc/workflow.md).

**Sample Output**

```
False 6,True 7104, Total 7110.
// Dots statistics
########
x = [69, 70, 71, 72, 72, 73]
y = [55, 55, 55, 55, 54, 53]
// two lists contains coordinate pairs
########
Range X Min: 69,Max: 73
Range Y Min: 53,Max: 55
// Domain & Range
```

### match

This program process the complex transforming action. Transforming from figure A to B, the program find the possible solution of matching, which makes the total distance moved short.

**Sample Output**

```
Point A[1] goes to point B[12].
Point A[6] goes to point B[19].
...
Point A[910] goes to point B[330].
Max (distance,point_in_B) to move:(15.0, 825)
Total distance: 10497.5672069
```

### km

A improvement in algorithm is made here. However, the KM algorithm requires a lot of computation when the distance matrix is large. Since the limited time, we cannot get the exact answer to this problem. But to exam the correctness of our program, here we set up a test to see if it working expectedly. For more information please view the [documentation](doc/workflow.md).

**Sample Input**

```
In text file M.txt:
[[9,4,3],[2,5,6],[7,1,8]] 
```

**Sample Output**

```
[1, 2, 0]
6
```

## Library

- numpy
- argparse
- PIL


## Environment

```
hisenzhang@hisenzhang-PC
OS: Deepin 15.4.1 unstable
Kernel: x86_64 Linux 4.9.0-deepin10-amd64
Shell: bash 4.4.11
Resolution: 1920x1080
CPU: Intel Core i5-7200U CPU @ 2.5GHz
GPU: Mesa DRI Intel(R) HD Graphics 620 (Kabylake GT2) 
RAM: 5124MiB / 7856MiB
Python: Python 2.7.13
MATLAB: R2016b on Linux
```

