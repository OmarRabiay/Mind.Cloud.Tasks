from PIL import Image

img = Image.open("Image.jpg") # Opens the image file

pixels = img.load()     
for x in range(int(img.width/4)): # Divides the width by 4 to select the first quarter
    for y in range(img.height):
        pixels[x, y] = (0, 0, 0)

img.save("Output.jpg") # Saves the new image
print("Image saved as Output.jpg")