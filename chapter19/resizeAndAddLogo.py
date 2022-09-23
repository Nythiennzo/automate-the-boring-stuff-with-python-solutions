   #! python3
   # resizeAndAddLogo.py - Resizes all images in current working directory to fit
   # in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

minimum_width = 2 * logoWidth
minimum_height = 2 * logoHeight

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    file_extention = filename.split('.')[-1].lower() if '.' in filename else ''
    if not (file_extention in ('png', 'jpg', 'gif', 'bmp')) or filename == LOGO_FILENAME:
        continue    # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    if width < minimum_width or height < minimum_height:
        continue

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))