Overview

This project demonstrates image transformations using linear algebra
and transformation matrices in Python.

The repository contains two programs:

Q10.py --- applies predefined 2×2 transformation matrices to an
image and analyzes their effect.

Q11.py --- provides an interactive image transformation toolbox.

The project connects mathematical concepts such as matrix
transformations, rank, basis-vector transformation, and information loss
with practical image processing.

Transformations Used in Q10

1. Scaling

[ A_1 =

\begin{bmatrix}
2 & 0\\
0 & 0.5
\end{bmatrix}

]

Stretches the image in one direction and compresses it in the other.

2. Rotation

[ A_2 =

\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}

]

Represents a 90° rotation.

3. Shearing

[ A_3 =

\begin{bmatrix}
1 & 1\\
0 & 1
\end{bmatrix}

]

Produces a shear transformation.

4. Reflection

[ A_4 =

\begin{bmatrix}
-1 & 0\\
0 & 1
\end{bmatrix}

]

Reflects points across the y-axis.

5. Projection

[ A_5 =

\begin{bmatrix}
1 & 0\\
0 & 0
\end{bmatrix}

]

Projects points onto the x-axis and results in dimension/information
loss.

Q10.py --- Matrix-Based Image Transformation

Q10.py loads an image and applies the five predefined transformation
matrices.

For every matrix, the program calculates:

T(e1)

T(e2)

Matrix rank

Whether dimension/information is lost

The transformed image

The image transformation is performed by representing each pixel
position relative to the image centre, multiplying that position by the
transformation matrix, and mapping the transformed position back to the
image.

Q11.py --- Image Transformation Toolbox

Q11.py is an interactive toolbox that allows the user to perform
different image transformations.

Available Options

1. Rotate
2. Resize
3. Flip
4. Shear
5. Custom Matrix
6. Reset
7. Exit

Rotation

Enter an angle in degrees to rotate the image around its centre.

Resize

Enter a resize factor to increase or decrease the image size.

Flip

The program supports:

Horizontal flip

Vertical flip

Shear

Enter a horizontal shear factor to apply a shear transformation.

Custom Matrix

The user can enter a custom 2×2 transformation matrix:

[ A =

\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}

]

The matrix is then applied to the image.

Technologies Used

Python

NumPy

Matplotlib

Pillow

OpenCV

Installation

Install the required libraries using:

pip install numpy matplotlib pillow opencv-python

How to Run

Run Q10

python Q10.py

Make sure the required image file is available in the project folder.

Run Q11

python Q11.py

The program will ask for the image filename:

Enter image filename (example: image.jpg):

After loading the image, choose an operation from the menu.

Project Structure

Image-Transformation/
│
├── Q10.py
├── Q11.py
├── image.jpg
└── README.md

Learning Objectives

This project helped me understand:

How matrices represent transformations.

How transformation matrices affect points and images.

How to calculate T(e1) and T(e2).

How matrix rank can be used to identify dimension/information loss.

How image pixels can be transformed mathematically.

How NumPy can be used for matrix operations.

How OpenCV can be used for image transformations.

How linear algebra concepts can be applied to practical image
processing.

Concepts Covered

Linear Transformations

Transformation Matrices

Basis Vectors

Matrix Rank

Information Loss

Scaling

Rotation

Reflection

Shearing

Projection

Image Processing

Author

Khushal Soni

IIT Jammu
Unified Engineering
