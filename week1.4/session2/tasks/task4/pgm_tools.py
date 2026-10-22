
# PGM functions that we write

from pathlib import Path


def readPGM(filename):
    '''
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''

    with open(filename, "r") as f:
        data = f.readlines()

    data = [line.strip().split() for line in data[1:]]

    width = int(data[0][0])
    height = int(data[0][1])
    max_gray = int(data[1][0])

    pixels = [[int(data[2+i][j]) for j in range(width)]
              for i in range(height)]

    return width, height, max_gray, pixels


def writePGM(filename, image):
    '''
    Write a PGM file to disk.
    Input: filename string, image tuple data
    Output: None
    '''

    width, height, max_gray, pixels = image

    with open(filename, "w") as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_gray}\n")

        for row in pixels:
            f.write(" ".join(str(pixel) for pixel in row) + "\n")


def invertPGM(image):
    '''
    Invert an image, ie. pixel value = max_gray - pixel value.
    Input: image data
    Output: inverted image data
    '''

    width, height, max_gray, pixels = image

    inverted = [[max_gray - pixels[i][j] for j in range(width)]
                for i in range(height)]

    return width, height, max_gray, inverted


# Code to test the PGM functions

# Find the folder containing this Python file
folder = Path(__file__).parent

# Read the original image
image = readPGM(folder / "images" / "feep.pgm")

print(f"Image with width {image[0]} and height {image[1]}")
print(image[3])

# Invert the image
inverted_image = invertPGM(image)

print("Inverted image:")
print(inverted_image[3])

# Write the inverted image to a new file
output_path = folder / "images" / "feep_inverted.pgm"
writePGM(output_path, inverted_image)

print(f"Inverted image saved to: {output_path}")

# Read the new file back in to check it
test_image = readPGM(output_path)

print("Image read back from file:")
print(test_image[3])
