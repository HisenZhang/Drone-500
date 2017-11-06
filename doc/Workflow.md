# Workflow
## Diagram

> Graphed by Hisen Zhang

```
+-----------------------------+    +----------------------+
|                             |    |                      |
|                             |    |                      |
|                             |    |                      |
|     Select a image          |    |                      |
|                             |    |     Curve fitting    |
|                             |    |                      |
|                             |    |                      |
|     Resize the picture      |    |                      |
|                             |    |               MATLAB |
|                             |    +----------^-----------+
|                             |               |
|     Convert to matrix       |               |
|                             |               |
|                             |               |
|                             |    +----------+-----------+
|     Preview and save        |    |                      |
|                             |    |    Cut into curves   |
|                             +---->                      |
|                      resize |    |            Photoshop |
+-----------------------------+    +----------------------+
```

## Description

### resize

`resize` is the program developed by ourselves. This program helps us to simplify following work:

1. Resize the picture to the geometry given. 
2. Convert the resized into 0-1 matrix. 

> This program is written with Python 2.7.  This is a free software; it is free for application, modification and distribution, but WITHOUT ANY WARRANTY and MERCHANTABILITY.

### Photoshop

Here `Photoshop` is used to decompose the graph into several curves. With each curve labeled, there is an equation which fits the curve.

### MATLAB

`MATLAB ` helps to work out the approximated equation of a given curve with the integrated 'curve fitting' function.