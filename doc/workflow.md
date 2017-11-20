# Workflow
## Diagram

> Graphed by Hisen Zhang

```
+-----------------------------+    +----------------------+
|                             |    |                      |
|                             |    |      Scheduling      |
|                             |    |                      |
|     Select an image         |    |             match.py |
|                             |    +----------^-----------+
|                             |               |
|                             |    +----------+-----------+
|     Resize the picture      |    |                      |
|                             |    |     Curve fitting    |
|                             |    |                      |
|                             |    |               MATLAB |
|     Convert to 0-1 matrix   |    +----------^-----------+
|                             |               |
|                             |    +----------+-----------+
|                             |    |                      |
|     Preview and save        |    |   Cut into labeled   |
|                             |    |       curves         |
|                             +---->                      |
|                   resize.py |    |            Photoshop |
+-----------------------------+    +----------------------+
```

## Description

### resize

> This program is written with Python 2.7.  This is a free software; it is free for application, modification and distribution, but WITHOUT ANY WARRANTY and MERCHANTABILITY.

`resize` is the program developed by ourselves. This program helps us to simplify following work:

1. Resize the picture to the geometry given. 
2. Convert the resized into 0-1 matrix. 
3. Get indexes of '1' elements.
4. Convert into conventional coordinate system as output.
5. Take domain and range.

The principle behind the resizing a picture is complicated. The algorithm we used here is **anti-aliasing**, which smooths the curve after its geometry is modified. For instance, if if you resize a circle into a low-resolution figure, it simply turns into dots which looks serrate. If an array of drones arrange so, it would be 'impressive' for all spectators - the figure is deformed thus hard to tell its shape. 

The second step employs the concept of **Threshold**. Basically if a pixel has a value greater than 128 it turns 1, else 0. Then we have a matrix consists of zeros and ones in our computer for further transformation.

Since there is an inconsistency in the coordination system between the conventional one and the computer one - the origin of computer's coordination system is on the left top - thus a conversion is needed. And this means we must revert the y-axis - It is not a tough tasks, though. Having the absolute value of the difference between given height and dots' y-value, the axis has been converted.

### Photoshop

Here `Photoshop` is used to decompose the graph into several curves. With each curve labeled, there is an equation which fits the curve.

### MATLAB

`MATLAB ` helps to work out the approximated equation of a given curve with the integrated 'curve fitting' function.

### match

> This program is written with Python 2.7.  This is a free software; it is free for application, modification and distribution, but WITHOUT ANY WARRANTY and MERCHANTABILITY.

Just like the first tool in workflow `resize`, we developed this program to achieve best possible moving schedule. Ideally, a best schedule may have following features:

- the total distance moved is minimized;
- the longest distance is minimized (it relates to worst time duration of moving);
- every path is valid for only one drone.


### km

> This program is written with Python 2.7.  This is a free software; it is free for application, modification and distribution, but WITHOUT ANY WARRANTY and MERCHANTABILITY.

The KM algorithm requires a lot of computation when the distance matrix is large. Since the limited time, we cannot get the exact answer to this problem. But to exam the correctness of our program, here we set up a test to see if it working expectedly.

Suppose we have a 3 by 3 matrix containing distance information and now we want to workout the minimum overall distance. 
$$
\left[\begin{matrix}9 & 4 & 3\\2 & 5 & 6 \\7 & 1 & 8\end{matrix}\right]
$$

```bash
$ echo [[9,4,3],[2,5,6],[7,1,8]] > tools/M.txt 
```

If we do it by hand, the '2' in first column seems to bring down the overall sum - thus we eliminate the second row. Then it is the third row, '1', and '3' in the first row. The expected answer is 6.

So that we applied an algorithm, KM. The program reads in a distance matrix `M.txt` and gives its output.

The output:

```bash
$ python tools/km.py 
[1, 2, 0]
6
```

The first line is a list, which indicate the index of selected element. In this case, '2', '1' and '3'. ( Remember the index of list starts with zero! ) The answer is just as what we have expected.

The minimum sum is given in the second line. 6.

Any other combination may lead to a sum which is equal or greater.