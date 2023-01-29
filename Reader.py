# Reader
# Inteligencia Artificial
# Mario de Leon 19019

from PIL import Image
import sys
import numpy as np


class Reader(object):
    def __init__(this, width, height, image):
        this.width = width
        this.height = height

        try:
            this.image = Image.open(image)
            # Resize
            size = (this.width, this.height)
            this.image = this.image.resize(size)
            # Save as bmp
            #this.image.save("map.bmp", "bmp")
        except:
            print("No se pudo cargar la imagen.")
            sys.exit(1)

    # Transform new picture replacing colors for easier work
    def transformer(this):
        redPixels = []
        greenPixels = []
        pixels = []
        this.image = this.image.convert('RGB')
        newMap = []
        startFull = False
        endFull = False
        width, height = this.image.size
        d = this.image.getdata()
        N = 100

        for item in d:
            # Red
            if item[0] in list(range(190, 255)) and item[1] in list(range(0, 100)) and item[2] in list(range(0, 100)):
                # print("red")
                if startFull == False:  # Only one red allowed
                    newMap.append((255, 0, 0))
                    pixels.append(2)
                    startFull = True
                else:
                    newMap.append((255, 255, 255))
                    pixels.append(0)
            # Green
            elif item[1] in list(range(150, 255)) and item[0] in list(range(0, 100)) and item[2] in list(range(0, 100)):
                # print("green")
                if endFull == False:  # Only one green allowed
                    newMap.append((0, 255, 0))
                    pixels.append(3)
                    endFull = True
                else:
                    newMap.append((255, 255, 255))
                    pixels.append(0)
            # Black
            elif item[0] in list(range(0, 50)) and item[1] in list(range(0, 50)) and item[2] in list(range(0, 50)):
                # print("black")
                newMap.append((0, 0, 0))
                pixels.append(1)
            # White
            else:
                newMap.append((255, 255, 255))
                pixels.append(0)
        this.image.putdata(newMap)
        this.image.save("map.bmp", "bmp")

        # Group elements in pixel list by the resolution N
        subPixels = [pixels[n:n+N] for n in range(0, len(pixels), N)]

        return subPixels
