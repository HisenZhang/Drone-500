# Drone 500

This repository contains files for Drone 500 Project.

## Files


```
.
├── doc		// documentation
├── img		// images used
│   ├── matrix	// processed images
│   └── raw	// raw images
│   └── separated	// the curves
├── map		// maps in .pdf
├── mat		// matrix in .mat and .xlsx
└── tools	// contains several ulitilies
```

## Utility

### resize

```
usage: resize.py [-h] [--output OUTPUT] input h w

positional arguments:
  input            Input file path.
  h                Height.
  w                Width.

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  Output file path.
```

This program basically functions in following pattern:

1. Resize the picture into the geometry given;
2. Convert to 0-1 matrix and save.
3. Get indexes of '1' elements.
4. Convert into conventional coordinate system as output.

For more information please view [documentation](./doc/workflow.md).

#### Sample Output

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

## Libraries

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

