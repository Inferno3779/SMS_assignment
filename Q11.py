import cv2
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# LOAD IMAGE
# --------------------------------------------------

filename = input("Enter image filename (example: image.jpg): ")

image = cv2.imread(filename)

if image is None:
    print("Error: Image not found.")
    exit()

# Convert BGR to RGB
original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Current image
img = original.copy()


# --------------------------------------------------
# DISPLAY IMAGE
# --------------------------------------------------

def display_image(img, title="Image"):

    plt.figure(figsize=(8, 6))
    plt.imshow(img)
    plt.title(title)
    plt.axis("off")
    plt.show()


# --------------------------------------------------
# ROTATE
# --------------------------------------------------

def rotate_image(img, angle):

    height, width = img.shape[:2]

    center = (width // 2, height // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    rotated = cv2.warpAffine(
        img,
        matrix,
        (width, height)
    )

    return rotated


# --------------------------------------------------
# RESIZE
# --------------------------------------------------

def resize_image(img, factor):

    height, width = img.shape[:2]

    new_width = int(width * factor)
    new_height = int(height * factor)

    resized = cv2.resize(
        img,
        (new_width, new_height)
    )

    return resized


# --------------------------------------------------
# FLIP
# --------------------------------------------------

def flip_image(img, direction):

    if direction == 1:
        # Horizontal flip
        return cv2.flip(img, 1)

    elif direction == 2:
        # Vertical flip
        return cv2.flip(img, 0)

    else:
        print("Invalid flip choice.")
        return img


# --------------------------------------------------
# SHEAR
# --------------------------------------------------

def shear_image(img, shear):

    height, width = img.shape[:2]

    matrix = np.array([
        [1, shear, 0],
        [0, 1,     0]
    ], dtype=np.float32)

    new_width = int(width + abs(shear) * height)

    sheared = cv2.warpAffine(
        img,
        matrix,
        (new_width, height)
    )

    return sheared


# --------------------------------------------------
# CUSTOM MATRIX
# --------------------------------------------------

def custom_matrix_image(img, a, b, c, d):

    height, width = img.shape[:2]

    # 2 x 2 transformation matrix
    A = np.array([
        [a, b],
        [c, d]
    ], dtype=np.float32)

    # Image centre
    cx = width / 2
    cy = height / 2

    # Transformation matrix for OpenCV
    matrix = np.array([
        [a, b, cx - a * cx - b * cy],
        [c, d, cy - c * cx - d * cy]
    ], dtype=np.float32)

    transformed = cv2.warpAffine(
        img,
        matrix,
        (width, height)
    )

    return transformed


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

while True:

    print("\n====================================")
    print("   IMAGE TRANSFORMATION TOOLBOX")
    print("====================================")

    print("1. Rotate")
    print("2. Resize")
    print("3. Flip")
    print("4. Shear")
    print("5. Custom Matrix")
    print("6. Reset")
    print("7. Exit")

    choice = input("\nEnter your choice: ")


    # ----------------------------------------------
    # ROTATE
    # ----------------------------------------------

    if choice == "1":

        angle = float(
            input("Enter rotation angle in degrees: ")
        )

        img = rotate_image(img, angle)

        display_image(img, "Rotated Image")


    # ----------------------------------------------
    # RESIZE
    # ----------------------------------------------

    elif choice == "2":

        factor = float(
            input("Enter resize factor (example: 2): ")
        )

        if factor <= 0:
            print("Resize factor must be greater than 0.")

        else:
            img = resize_image(img, factor)

            display_image(img, "Resized Image")


    # ----------------------------------------------
    # FLIP
    # ----------------------------------------------

    elif choice == "3":

        print("\n1. Horizontal Flip")
        print("2. Vertical Flip")

        direction = int(
            input("Enter your choice: ")
        )

        img = flip_image(img, direction)

        display_image(img, "Flipped Image")


    # ----------------------------------------------
    # SHEAR
    # ----------------------------------------------

    elif choice == "4":

        shear = float(
            input("Enter horizontal shear factor: ")
        )

        img = shear_image(img, shear)

        display_image(img, "Sheared Image")


    # ----------------------------------------------
    # CUSTOM MATRIX
    # ----------------------------------------------

    elif choice == "5":

        print("\nEnter the 2 x 2 transformation matrix:")

        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = float(input("Enter d: "))

        print("\nYour matrix is:")
        print(
            np.array([
                [a, b],
                [c, d]
            ])
        )

        img = custom_matrix_image(
            img, a, b, c, d
        )

        display_image(img, "Custom Matrix Transformation")


    # ----------------------------------------------
    # RESET
    # ----------------------------------------------

    elif choice == "6":

        img = original.copy()

        print("Image has been reset.")

        display_image(img, "Original Image")


    # ----------------------------------------------
    # EXIT
    # ----------------------------------------------

    elif choice == "7":

        print("\nToolbox closed.")
        break


    # ----------------------------------------------
    # INVALID CHOICE
    # ----------------------------------------------

    else:

        print("Invalid choice. Please select 1-7.")