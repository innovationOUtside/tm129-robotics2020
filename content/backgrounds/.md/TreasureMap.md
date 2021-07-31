---
jupyter:
  jupytext:
    formats: ipynb,.md//md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python activity=true commentate=true
#%pip install noise
```

```python
#https://github.com/Zibe/ProceduralTreasureMap/

from queue import Queue
from noise import pnoise2, snoise2
from PIL import Image, ImageFont, ImageDraw
import random
#import IslandNameGenerator

noiseResolution = 0.01
noiseOctave = 4
noiseFrequency = 16 * noiseOctave

mapScale = 75
mapLineSize = 2

time = 0
timeChange = 1

islandList = []
nameList = []

global width
global height

imgPadding = 75

seaLevel = 0.15
landLevel = 0.2


class Island:

    def __init__(self):
        self.pixels = []
        self.minX = width
        self.maxX = 0
        self.minY = height
        self.maxY = 0

    def addPixel(self, coord, noise):
        #Compute bounding box
        self.minX = min(self.minX, coord[0])
        self.maxX = max(self.maxX, coord[0])
        self.minY = min(self.minY, coord[1])
        self.maxY = max(self.maxY, coord[1])

        self.pixels.append((coord[0], coord[1], noise))

    def getSurface(self):
        return (self.maxX - self.minX) * (self.maxY - self.minY)


def boxCollison( box1, box2):

    return box1[0] < box2[2] and  box1[2] > box2[0] and box1[1] < box2[3] and box1[3] > box2[1]

def generateMap():

    # Generate noise texture
    seed = random.random() * 1000
    xoff = seed
    noiseValues = [[-1] * height for i in [-1] * width]
    for x in range(imgPadding, width):
        xoff += noiseResolution
        yoff = seed
        for y in range(imgPadding, height):
            yoff += noiseResolution
            noiseValues[x][y] = pnoise2(xoff, yoff, noiseOctave)


    # Fill the island list using flood fill
    marks = [[-1] * height for i in [-1] * width]
    for x in range(imgPadding, width):
        for y in range(imgPadding, height):
            if marks[x][y] == -1:
                if noiseValues[x][y] < seaLevel:
                    marks[x][y] = 0
                else:
                    q = Queue()
                    q.put((x,y))
                    island = Island()
                    while q.empty() is False:
                        index = q.get()
                        for i in range(max(0, index[0] - 1), min(index[0] + 2, width)):
                            for j in range(max(0, index[1] - 1), min(index[1] + 2, height)):
                                if marks[i][j] == -1:
                                    if noiseValues[i][j] < seaLevel:
                                        marks[i][j] = 0
                                    else:
                                        marks[i][j] = 1
                                        island.addPixel((i,j), noiseValues[i][j])
                                        q.put((i,j))
                    islandList.append(island)

def drawNames( draw ):

    #Big messy code which computes potentials bounding boxes for text and choose the bigger one
    #Avoid collisions with islands and other names
    for i in islandList:
        if i.getSurface() > 2000:
            text = ''#IslandNameGenerator.generateName()
            shadowcolor = "black"

            #font credits : https://www.fontsquirrel.com/fonts/kristi
            font = ImageFont.truetype("Kristi.ttf", 24)
            fontSize = draw.textsize(text, font)

            topBox = [max((i.maxX - i.minX) / 2 - fontSize[0], imgPadding), max(i.minY - fontSize[1], imgPadding),
                      min((i.maxX - i.minX) / 2 + fontSize[0], width), i.minY]
            leftBox = [max(i.minX - fontSize[0], imgPadding), i.minY, i.minX, i.maxY]
            rightBox = [i.maxX, i.minY, min(i.maxX + fontSize[0], width), i.maxY]
            bottomBox = [max((i.maxX - i.minX) / 2 - fontSize[0], imgPadding), i.maxY,
                         min((i.maxX - i.minX) / 2 + fontSize[0], width), min(i.maxY + fontSize[1], height)]

            for j in nameList:
                if i != j:
                    box = [j[0], j[1], j[2], j[3]]
                    if boxCollison(box, leftBox):
                        if leftBox[1] > box[1]:
                            leftBox[1] = max(leftBox[1], box[3])
                        elif leftBox[3] < box[3]:
                            leftBox[3] = min(leftBox[3], box[1])
                        else:
                            leftBox[0] = max(leftBox[0], box[2])
                    if boxCollison(box, rightBox):
                        if rightBox[1] > box[1]:
                            rightBox[1] = max(rightBox[1], box[3])
                        elif rightBox[3] < box[3]:
                            rightBox[3] = min(rightBox[3], box[1])
                        else:
                            rightBox[2] = min(rightBox[2], box[0])
                    if boxCollison(box, topBox):
                        if topBox[0] > box[0]:
                            topBox[0] = max(topBox[0], box[2])
                        elif topBox[2] < box[2]:
                            topBox[2] = min(topBox[2], box[0])
                        else:
                            topBox[1] = max(topBox[1], box[3])
                    if boxCollison(box, bottomBox):
                        if bottomBox[0] > box[0]:
                            bottomBox[0] = max(bottomBox[0], box[2])
                        elif topBox[2] < box[2]:
                            bottomBox[2] = min(bottomBox[2], box[0])
                        else:
                            bottomBox[1] = min(bottomBox[3], box[1])

            for j in islandList:
                if i != j:
                    box = [j.minX, j.minY, j.maxX, j.maxY]
                    if boxCollison(box, leftBox):
                        if leftBox[1] > box[1]:
                            leftBox[1] = max(leftBox[1], box[3])
                        elif leftBox[3] < box[3]:
                            leftBox[3] = min(leftBox[3], box[1])
                        else:
                            leftBox[0] = max(leftBox[0], box[2])
                    if boxCollison(box, rightBox):
                        if rightBox[1] > box[1]:
                            rightBox[1] = max(rightBox[1], box[3])
                        elif rightBox[3] < box[3]:
                            rightBox[3] = min(rightBox[3], box[1])
                        else:
                            rightBox[2] = min(rightBox[2], box[0])
                    if boxCollison(box, topBox):
                        if topBox[0] > box[0]:
                            topBox[0] = max(topBox[0], box[2])
                        elif topBox[2] < box[2]:
                            topBox[2] = min(topBox[2], box[0])
                        else:
                            topBox[1] = max(topBox[1], box[3])
                    if boxCollison(box, bottomBox):
                        if bottomBox[0] > box[0]:
                            bottomBox[0] = max(bottomBox[0], box[2])
                        elif topBox[2] < box[2]:
                            bottomBox[2] = min(bottomBox[2], box[0])
                        else:
                            bottomBox[1] = min(bottomBox[3], box[1])

            leftSpace = (leftBox[3] - leftBox[1]) * (leftBox[2] - leftBox[0])
            rightSpace = (rightBox[3] - rightBox[1]) * (rightBox[2] - rightBox[0])
            topSpace = (topBox[3] - topBox[1]) * (topBox[2] - topBox[0])
            bottomSpace = (bottomBox[3] - bottomBox[1]) * (bottomBox[2] - bottomBox[0])

            maxSpace = max(leftSpace, rightSpace, topSpace, bottomSpace)

            if maxSpace == leftSpace:
                x = leftBox[0]
                y = leftBox[1]
            elif maxSpace == rightSpace:
                x = rightBox[2] - fontSize[0]
                y = rightBox[1]
            elif maxSpace == topSpace:
                x = topBox[0]
                y = topBox[1]
            else:
                x = bottomBox[0]
                y = bottomBox[3] - fontSize[1]

            draw.text((x, y), text, font=font, fill=shadowcolor)
            nameList.append((x, y, x + fontSize[0], y + fontSize[1]))

def drawCross( draw ):

    validIslands = list()
    for i in islandList:
        if i.getSurface() > 1000 :
            validIslands.append(i)

    isleIndex = random.randrange(0, len(validIslands))
    pixelIndex = random.randrange(0, len(validIslands[isleIndex].pixels))

    pixel = validIslands[isleIndex].pixels[pixelIndex]

    q1 = Queue()
    q1.put((pixel[0] - 5, pixel[1] - 5))
    q1.put((pixel[0] + 5, pixel[1] + 5))
    q1.put((pixel[0] + 3, pixel[1] + 7))
    q1.put((pixel[0] - 7, pixel[1] - 3))


    q2 = Queue()
    q2.put((pixel[0] - 5, pixel[1] + 5))
    q2.put((pixel[0] + 5, pixel[1] - 5))
    q2.put((pixel[0] + 3, pixel[1] - 7))
    q2.put((pixel[0] - 7, pixel[1] + 3))

    #Slightly shifth cross'lines in order to make it look hand drawn
    for i in range(100) :
        a = q1.get()
        b = q1.get()
        middle = (a[0] + b[0])/ 2 , (a[1] + b[1]) / 2
        middle = random.gauss(middle[0], 0.1), random.gauss(middle[1], 0.1)
        q1.put(a)
        q1.put(middle)
        q1.put(b)

        a = q2.get()
        b = q2.get()
        middle = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        middle = random.gauss(middle[0], 0.1), random.gauss(middle[1], 0.1)
        q2.put(a)
        q2.put(middle)
        q2.put(b)


    draw.polygon(list(q1.queue),  "red")
    draw.polygon(list(q2.queue), "red")


#I do not own any right on the parchment texture, and I didn't add it to the Git. Feel free to use your
#img = Image.open("parchment.png")
img = Image.new("RGB", (800, 600), (255, 255, 255))

new_im = Image.new('RGBA', (img.size[0], img.size[1]))
global width, height
width = img.size[0] - imgPadding
height = img.size[1] - imgPadding
pixels = img.load()
new_pxl = new_im.load()

#copy texture (I was tired)
for x in range(img.size[0]):
    for y in range(img.size[1]):
            new_pxl[x,y] = pixels[x,y]
draw = ImageDraw.Draw(new_im)

#longitude and latitude line
for y in range(imgPadding, height, int((height - imgPadding) / 4) + 1):
    draw.line(((imgPadding, y), (width, y)), "black")
for x in range(imgPadding, width, int((width - imgPadding) / 7) + 1):
    draw.line(((x, imgPadding), (x, height)), "black")

generateMap()
for i in islandList:
    for pixel in i.pixels:
        if pixel[2] > landLevel :
            #If land, draw the texure over the lines
            new_pxl[pixel[0], pixel[1]] = pixels[pixel[0], pixel[1]]
        else:
            new_pxl[pixel[0], pixel[1]] = (0,0,0,255)

drawNames(draw)
drawCross(draw)

#Draw Islands's Bounding boxes
    #draw.line(((i.minX, i.minY), (i.maxX, i.minY),
    #          (i.minX, i.minY), (i.minX, i.maxY),
    #           (i.minX, i.maxY), (i.maxX, i.maxY),
    #           (i.maxX, i.minY), (i.maxX, i.maxY)
    #           ), "white")


draw.rectangle(((imgPadding, imgPadding), (width, height)), None, "black")

del draw

new_im.save("out.png")
new_im

```

```python
new_im
```

```python

```
