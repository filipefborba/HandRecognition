# import os

# classnames = ["palm", "l", "fist", "fist_moved", "thumb", "index", "ok", "palm_moved", "c", "down"]

import os

# We need to get all the paths for the images to later load them
imagepaths = []

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
       path = os.path.join(root, name)
       if path.endswith("png"): #We want only the images
           imagepaths.append(path)

print(len(imagepaths)) # If > 0, then a PNG image was loaded

for i in imagepaths:
    print(i.split("\\")[3])