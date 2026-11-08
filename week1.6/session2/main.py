from image import Image, ImageError

# TASK 1 - Create an image

img = Image.create(5, 5)

print("TASK 1: Create an image")
print("Width:", img.width)
print("Height:", img.height)
print("Pixels:", img.pixels)


# TASK 2 - Change pixels

print("\nTASK 2: Change pixels")

img.set(0, 0, 255)
img.set(1, 1, 150)
img.set(2, 2, 100)
img.set(3, 3, 50)
img.set(4, 4, 0)

print("Pixel at (0, 0):", img.get(0, 0))
print("Pixel at (1, 1):", img.get(1, 1))
print("Pixel at (2, 2):", img.get(2, 2))
print("All pixels:", img.pixels)


# TASK 3 - Copy an image

print("\nTASK 3: Copy an image")

img_copy = img.copy()

img_copy.set(0, 0, 100)

print("Original image pixel:", img.get(0, 0))
print("Copied image pixel:", img_copy.get(0, 0))


# TASK 4 - Read an image

print("\nTASK 4: Read an image")

try:
    loaded_img = Image.read("/images/coins.pgm")

    print("Width:", loaded_img.width)
    print("Height:", loaded_img.height)
    print("Pixels:", loaded_img.pixels)

except FileNotFoundError:
    print("PGM file not found. Check the filename and directory.")


# TASK 5 - Save an image

print("\nTASK 5: Save an image")

img.write_pgm("example.pgm")

print("Image successfully saved as example.pgm")


# TASK 6 - Error handling

print("\nTASK 6: Error handling")

try:
    invalid_img = Image.create(0, 5)

except ImageError as error:
    print("Width error:", error)


try:
    invalid_img = Image.create(5, 0)

except ImageError as error:
    print("Height error:", error)