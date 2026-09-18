import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
img = Image.open("image.jpg").convert("RGB")

# Transformation matrices
A1 = np.array([[2, 0],
               [0, 0.5]])

A2 = np.array([[0, -1],
               [1,  0]])

A3 = np.array([[1, 1],
               [0, 1]])

A4 = np.array([[-1, 0],
               [0,  1]])

A5 = np.array([[1, 0],
               [0, 0]])


def transform_image(img, A):

    img = np.array(img)

    height, width = img.shape[:2]

    cx = width / 2
    cy = height / 2

    result = np.zeros_like(img)

    for y in range(height):
        for x in range(width):

            point = np.array([x - cx, y - cy])

            new_point = A @ point

            new_x = int(new_point[0] + cx)
            new_y = int(new_point[1] + cy)

            if 0 <= new_x < width and 0 <= new_y < height:
                result[new_y, new_x] = img[y, x]

    return result


matrices = [A1, A2, A3, A4, A5]

for i, A in enumerate(matrices, 1):

    print("\nA" + str(i) + " =")
    print(A)

    # (a) T(e1) and T(e2)
    print("T(e1) =", A[:, 0])
    print("T(e2) =", A[:, 1])

    # (c) Rank
    print("Rank =", np.linalg.matrix_rank(A))

    # (d) Information loss
    if np.linalg.matrix_rank(A) < 2:
        print("Dimension/Information lost: YES")
    else:
        print("Dimension/Information lost: NO")

    # Transform image
    if i == 5:
        print("True A5 matrix is:")
        print(A)

        # Only for visualization
        visual_A = np.array([[1, 0],
                             [0, 0.01]])

        transformed = transform_image(img, visual_A)

    else:
        transformed = transform_image(img, A)

    # Display
    plt.figure(figsize=(6, 5))
    plt.imshow(transformed)
    plt.title("Transformation A" + str(i))
    plt.axis("off")
    plt.show()