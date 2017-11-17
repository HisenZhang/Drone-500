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

