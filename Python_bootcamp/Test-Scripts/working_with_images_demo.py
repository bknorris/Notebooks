# -*- coding: utf-8 -*-
"""
Demo for image processing, based on the
Complete-python-bootcamp on udemy.com


"""

from PIL import Image

# Let's open some images!
path = 'c:\\Users\\bknorris\\Documents\\Scripts\\Python\\Python_bootcamp\\Complete-Python-3-Bootcamp\\14-Working-with-Images\\'

mac = Image.open(path + 'example.jpg')

# Display image with mac.show()
# Get size with mac.size
# Get filename with mac.filename and format with mac.format_description

# Crop the image (origin at top left)
mac.crop((0, 0, 100, 100))

# Let's try another example
pencils = Image.open(path + 'pencils.jpg')

# pencils.size returns (1950,1300)
x = 0
y = 0
w = 1950 / 3
h = 1300 / 10
pencils.crop((x, y, w, h))

# Copy and pasting images, let's use that mac image again
halfway = 1993 / 2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
computer = mac.crop((x, y, w, h)) # assign crop to new object
mac.paste(im=computer, box=(0,0)) # tuple defines paste location

# Display the image with mac.show()

# Resize image
mac.resize((100, 80))

# Rotate
mac.rotate(90)

# Transparency
# Images have RGBA (0 - 255)
# if A = 0, the image is transparent, if it's 255, it's opaque
red = Image.open(path + 'red_color.jpg')
blue = Image.open(path + 'blue_color.png')

# Change image alpha
red.putalpha(155)
red.show()

# Save an image
red.save(path + "new_red.png")
