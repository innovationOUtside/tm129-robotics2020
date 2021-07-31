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

# Generate Background Images for `ev3devsim` Robot Simulator

Simple routes for generating png files for use in `ev3devsim` robot simulator.

Image size: width 2362px, height 1143px.

*Could be useful to support interactive canvas drawing of backgrounds too?*

In the Docker container, background originals are in `/srv/conda/envs/notebook/lib/python3.7/site-packages/nbev3devsim/backgrounds/`. Find paths via: `python -m site`

```python
from IPython.display import Image as I
from PIL import Image, ImageDraw


mode = 'RGB'
size = (2362, 1143)
color = 'white'
```

It is possible to add metadata text to PNG images ([docs](https://dev.exiv2.org/projects/exiv2/wiki/The_Metadata_in_PNG_files); [example](https://stackoverflow.com/a/58399815/454773)), which could provide a way of getting config information into the simulator setup. As well as writing metadata into the image, we also need to extract it (using something like [this](https://github.com/hometlt/png-metadata) maybe?).


## Blank Image

```python
filename = '_backgrounds/_blank.png'

img = Image.new(mode, size, color)
img.save(filename)
```

## Greys

```python
filename = '_backgrounds/_greys.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)

x_init = 250
x_width = 200
x_gap = x_width
y_init = 150
y_height = 750
diam = 100

for fill in ['gainsboro', 'lightgrey', 'grey', 'black']:
    draw.rectangle([(x_init, y_init), (x_init+x_width, y_init+y_height)], fill=fill)
    x_init = x_init + x_width + x_gap
#draw.rectangle([(800, 300), (1000, 900)], fill='gainsboro')
#draw.rectangle([(1200, 300), (1400, 900)], fill='lightgrey')
#draw.rectangle([(1600, 300), (1800, 900)], fill='grey')
#draw.rectangle([(2000, 300), (2200, 900)], fill='black')


y_h = y_init + diam
for fill in ['#FF0000', '#00FF00', '#0000FF']:
    draw.ellipse((x_init, y_h, x_init + diam, y_h + diam), fill = fill)
    y_h += 2 * diam

img.save(filename)
I(filename)
```

## Coloured Bands

```python
filename = '_backgrounds/_coloured_bands.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)

x_init = 250
x_width = 200
x_gap = x_width
y_init = 150
y_height = 600

for fill in ['#FF0000', '#00FF00', '#0000FF', '#000000']:
    draw.rectangle([(x_init, y_init), (x_init+x_width, y_init+y_height)], fill=fill)
    x_init = x_init + x_width + x_gap
    
#draw.rectangle([(800, 300), (1000, 900)], fill='#FF0000')
#draw.rectangle([(1200, 300), (1400, 900)], fill='#00FF00')
#draw.rectangle([(1600, 300), (1800, 900)], fill='#0000FF')
#draw.rectangle([(2000, 300), (2200, 900)], fill='#000000')
img.save(filename)
I(filename)
```

```python
filename = '_backgrounds/_rainbow_bands.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)

_delta_w = 200
_w = 200

y_init = 150
y_height = 600

for c in ['#FF0000', '#00FF00', '#0000FF', '#00FFFF', '#FF00FF', '#FFFF00', '#000000']:
    draw.rectangle([(_w, y_init), (_w+_delta_w, y_init+y_height)], fill=c)
    _w += _delta_w
img.save(filename)
I(filename)
```

## Grey and Black

```python
filename = '_backgrounds/_grey_and_black.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)

striped_band = 600
long_band = 100
band_height = 100

left_origin = 200
band_width = 400

#Black band
draw.rectangle([(left_origin, long_band), (left_origin + 4 * band_width, long_band + band_height)], fill='black')

#Light grey / black / grey band
draw.rectangle([(left_origin, striped_band), (left_origin + band_width, striped_band + band_height)], fill='lightgrey')
draw.rectangle([(left_origin + band_width, striped_band), (left_origin + 2 * band_width, striped_band + band_height)], fill='black')
draw.rectangle([(left_origin + 2 * band_width, striped_band), (left_origin + 3 * band_width, striped_band + band_height)], fill='gainsboro')
draw.rectangle([(left_origin + 3 * band_width, striped_band), (left_origin + 4 * band_width, striped_band + band_height)], fill='grey')

img.save(filename)
I(filename)
```

## Square

```python
filename = '_backgrounds/_square.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)

draw.rectangle([(600, 400), (1000, 800)], fill='grey')
  
draw.rectangle([(300, 100), (1300, 1100)], outline ="grey", width=20) 

img.save(filename)
I(filename)
```

## Loop

```python
#https://stackoverflow.com/questions/7787375/python-imaging-library-pil-drawing-rounded-rectangle-with-gradient/50145023#50145023
#from PIL.ImageDraw import ImageDraw

def rounded_rectangle(self: ImageDraw, xy, corner_radius, fill=None, outline=None):
    upper_left_point = xy[0]
    bottom_right_point = xy[1]
    self.rectangle(
        [
            (upper_left_point[0], upper_left_point[1] + corner_radius),
            (bottom_right_point[0], bottom_right_point[1] - corner_radius)
        ],
        fill=fill,
        outline=outline
    )
    self.rectangle(
        [
            (upper_left_point[0] + corner_radius, upper_left_point[1]),
            (bottom_right_point[0] - corner_radius, bottom_right_point[1])
        ],
        fill=fill,
        outline=outline
    )
    self.pieslice([upper_left_point, (upper_left_point[0] + corner_radius * 2, upper_left_point[1] + corner_radius * 2)],
        180,
        270,
        fill=fill,
        outline=outline
    )
    self.pieslice([(bottom_right_point[0] - corner_radius * 2, bottom_right_point[1] - corner_radius * 2), bottom_right_point],
        0,
        90,
        fill=fill,
        outline=outline
    )
    self.pieslice([(upper_left_point[0], bottom_right_point[1] - corner_radius * 2), (upper_left_point[0] + corner_radius * 2, bottom_right_point[1])],
        90,
        180,
        fill=fill,
        outline=outline
    )
    self.pieslice([(bottom_right_point[0] - corner_radius * 2, upper_left_point[1]), (bottom_right_point[0], upper_left_point[1] + corner_radius * 2)],
        270,
        360,
        fill=fill,
        outline=outline
    )


ImageDraw.ImageDraw.rounded_rectangle = rounded_rectangle

```

```python
filename = '_backgrounds/_loop.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)
draw.rounded_rectangle([(200, 200), (1900, 1000)], 80, fill='black')
draw.rounded_rectangle([(300, 300), (1800, 900)], 50, fill='white')
img.save(filename)
I(filename)
```

```python
filename = '_backgrounds/_two_shapes.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)
draw.rounded_rectangle([(200, 400), (700, 900)], 80, fill='black')
draw.rounded_rectangle([(300, 500), (600, 800)], 50, fill='white')


outline = 100 # line thickness
draw.ellipse((1200, 400, 1700, 900), fill='black')
draw.ellipse((1200+outline, 400+outline, 1700-outline, 900-outline), fill='white')

img.save(filename)
I(filename)
```

## Linear Gradient

A graduated grey background that is black at the bottom and white at the top.

```python
filename = '_backgrounds/_linear_grey.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)

# White edge
draw.line([0, 100, size[0], 100], width=100, fill=(255,255,255))
#Black edge
draw.line([0, size[1]-100, size[0], size[1]-100], width=100, fill=(0,0,0))


_scaler = (size[1]-200)/256
for y in range(100, (size[1]-100)):
    _y = 255-int(255*(y-100)/(size[1]-200))
    draw.line([0, y, size[0], y], width=1, fill=(_y,_y,_y))


img.save(filename)

I(filename)
```

## Radial Gradient (Braitenberg)

```python
import math

img = Image.new(mode, size, color)


innerBlue = [80, 80, 255] #Color at the center
outerBlue = [0, 0, 80] #Color at the corners
blues = ('_backgrounds/_radial_blue.png', innerBlue, outerBlue)

innerRed = [255, 80, 80] #Color at the center
outerRed = [80, 0, 0] #Color at the corners
reds = (_backgrounds/'_radial_red.png', innerRed, outerRed)

innerGrey = [255, 255, 255] #Color at the center
outerGrey = [0, 0, 0] #Color at the corners
greys = ('_backgrounds/_radial_grey.png', innerGrey, outerGrey)


#https://stackoverflow.com/a/30669765/454773
def radial(img, radial_config):
    """Generate a radial gradient image."""
    (filename, innerColor, outerColor) = radial_config
    for y in range(size[1]):
        for x in range(size[0]):

            #Find the distance to the center
            distanceToCenter = math.sqrt((x - size[0]/2) ** 2 + (y - size[1]/2) ** 2)

            #Make it on a scale from 0 to 1
            distanceToCenter = float(distanceToCenter) / (math.sqrt(2) * size[0]/2)

            #Make non-linear
            #distanceToCenter = math.sqrt(distanceToCenter)
            distanceToCenter = distanceToCenter**(1./3.)
            
            #Calculate r, g, and b values
            r = outerColor[0] * distanceToCenter + innerColor[0] * (1 - distanceToCenter)
            g = outerColor[1] * distanceToCenter + innerColor[1] * (1 - distanceToCenter)
            b = outerColor[2] * distanceToCenter + innerColor[2] * (1 - distanceToCenter)

            #Place the pixel        
            img.putpixel((x, y), (int(r), int(g), int(b))) 
    
    img.save(filename)
    return filename, img

filename, _ = radial(img, blues)
I(filename)

filename, _ = radial(img, reds)
I(filename)

filename, _ = radial(img, greys)
I(filename)
```

## Line Follower

```python
filename = '_backgrounds/_line_follower_track.png'

img = Image.new(mode, size, 'lightgrey')
draw = ImageDraw.Draw(img)

x, y =  img.size
#Size of Bounding Box for ellipse
eX, eY = 1000, 400

inset = 400
outerBox =  (inset, y/2 - eY/2, inset + eX/2, y/2 + eY/2)
exitBox1 = (inset - 20 + eX/2, y/2 + -100, 4000 + eX/2, y/2 + 50 )
exitBox2 = (inset - 18 + eX/2, y/2 + -100, 4000 + eX/2, y/2 + 100 )

draw.ellipse(outerBox, outline ="black", width=20)

draw.rectangle((inset + eX/2 - 40, y/2 - 49, inset + eX/2 + 20, y/2+22), fill='lightgrey')


_ly = -22
_lx = -22
_lh = 95
_lo = -75

# Arc: bounding box, start angle, end angle
draw.arc((inset + _lx + eX/2, y/2 + _ly,
          inset + _lx + eX/2 + 200, y/2 + _ly + _lh ),
         start = 180, end = 270, width=20, fill ="black")
draw.arc((inset + _lx + eX/2 - 4, y/2 + _ly + _lo,
          inset + _lx + eX/2 + 200, y/2 + _ly + _lh + _lo),
         start = 90, end = 180, width=20, fill ="black")

# This needs fixing properly / relatively; maybe even some sums!
draw.rectangle((1700 - 20, y/2 - 200, 1700 + 20, y/2 + 200), fill ="yellow") 
draw.rectangle((inset + eX/2 +15, y/2 - 22, 1900, y/2), fill ="black") 
draw.rectangle((1900 - 20, y/2 - 200, 1900 + 20, y/2 + 200), fill ="red") 
 

#draw.rectangle([(800, 300), (1000, 900)], fill='gainsboro')
img.save(filename)
I(filename)
```

```python
%pip install noisify
from noisify.recipes import human_error, machine_error
combined_noise = machine_error(20) + human_error(15)
[i for i in combined_noise(img)][0]
```

```python
from PIL import ImageFilter
tmp = img
for i in range(10):
    tmp = tmp.filter(ImageFilter.BLUR) # BLUR, SMOOTH

tmp

```

```python
#https://stackoverflow.com/a/59991417/454773
import numpy as np
def add_salt_and_pepper(image, amount):

    output = np.copy(np.array(image))

    # add salt
    nb_salt = np.ceil(amount * output.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(nb_salt)) for i in output.shape]
    output[tuple(coords)] = 1

    # add pepper
    nb_pepper = np.ceil(amount* output.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(nb_pepper)) for i in output.shape]
    output[tuple(coords)] = 0

    return Image.fromarray(output)

add_salt_and_pepper(img,0.01)
```

```python
noisy_image = add_salt_and_pepper(img,0.1).filter(ImageFilter.GaussianBlur(7))
noisy_image.save(f'_backgrounds/_noisy{filename}')
noisy_image
```

```python
# Cropped image 
border = 10
start_x = inset+50
im1 = img.crop((start_x + eX/2 - border, y/2 - border, start_x + eX/2 + border, y/2+border)) 
resize = (300, 300) 
im1 = im1.resize(resize)  
im1 
```

### Zooming widget

May be better to do this in js? eg this looks nice, but how accessible is it? https://mark-rolich.github.io/Magnifier.js/

```python
from ipywidgets import interact
    
@interact(x=(border, size[0]-border),
          y=(border, size[1]-border),
          border=[('5px', 5), ('10px', 10), ('20px', 20), ('30px',30)],
          continuous_update=False)
def image_zoom(x=100, y=100, border="10px"):
    """Zoom into part of image."""

    im1 = img.crop((x - border, y - border,
                    x + border, y + border)) 
    resize = (300, 300) 
    im1 = im1.resize(resize)
    im2 = img.copy().resize((size[0], size[1]))
    draw = ImageDraw.Draw(im2)
  
    draw.rectangle([(x - border, y - border), (x + border, y + border)],
                   outline ="blue", width=1) 

    display(im2)
    display(im1)
```

```python

```

### Filtering

```python
img.filter(ImageFilter.MedianFilter)
```

<!-- #raw -->

from tqdm.auto import trange
output = np.copy(np.array(img))
for i in trange(np.array(img).shape[0]):
    if np.random.random() < 0.1:
        for j in range(np.array(img).shape[1]):
            if np.random.random() < 0.1:
                for k in range(np.array(img).shape[2]):
                    output[i][j][k] = max(min(output[i][j][k]+np.random.randint(100)-50, 255), 0)
Image.fromarray(output)
<!-- #endraw -->

## Sensor Diameter Test

```python
filename = '_backgrounds/_sensor_diameter_test.png'

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)

_band_thickness = 2
_band_length = size[0]

_band_gap = 80
_band_gap_h = 40
_xh0 = 200
_xh = _xh0
_band_x0 = 0
_band_y0 = 200

_x = _band_x0
_y = 0

def bands(colour='black'):
    """Plot a series of bands."""
    for i in range(5):
        _y = _band_y0 + i*_band_gap_h
        _xh = _xh0 + 2 * i * (_band_gap_h - _band_thickness/2)
        draw.rectangle([(_x, _y),
                        (_x + _band_length, _y + i * _band_thickness)], fill=colour)
        
        draw.rectangle([(_xh, 0), (_xh + i * _band_thickness, size[1])], fill=colour)
        
        _xh = _xh + _band_gap_h
        draw.rectangle([(_xh, 0), (_xh + i * _band_thickness, size[1])], fill=colour)

draw.ellipse((_xh-5, _band_y0-5, _xh+5, _band_y0+5), outline ='blue')
draw.ellipse((_xh+35, _band_y0-5, _xh+45, _band_y0+5), outline ='blue')

bands()

_band_y0 = _y + 8 * _band_gap
_xh0 = 1000
bands('red')

    
img.save(filename)
I(filename)
```

## Simple sensor shapes

Test track that contains some simple shapes along a line.

```python
filename = '_backgrounds/_simple_shapes.png'

import math

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)

_side = 10

_x_delta = 80
_y_delta = 0


_centre_offset_x = 25
_centre_offset_y = 18

def _polygon_square(_x, _y, _side, draw, fill='black', mod=-4):
    _side = _side + mod
    _x += _centre_offset_x - mod/2
    _y += _centre_offset_y - mod/2
    draw.rectangle([(_x, _y), (_x + _side, _y + _side)], fill=fill)

def polygon_circle(_x, _y, _side, draw, fill='black', mod=-4):
    _side = _side + mod
    _x += _centre_offset_x - mod/2
    _y += _centre_offset_y - mod/2
    draw.ellipse((_x, _y, _x + _side, _y + _side), fill=fill)

def polygon_equitriangle1(_x, _y, _side, draw, fill='black'):
    _x += _centre_offset_x
    _y += _centre_offset_y
    _x += 2
    draw.polygon(((_x, _y), (_x, _y + _side), (_x + math.sqrt(3) * _side / 2, _y + _side / 2 )), fill=fill)

def polygon_equitriangle2(_x, _y, _side, draw, fill='black'):
    _x += _centre_offset_x
    _y += _centre_offset_y
    draw.polygon(((_x, _y + _side / 2 ), (_x + math.sqrt(3) * _side / 2, _y),
                  (_x + math.sqrt(3) * _side / 2, _y + _side)), fill=fill)

def polygon_equitriangle3(_x, _y, _side, draw, fill='black'):
    _x += _centre_offset_x
    _y += _centre_offset_y
    _y += 2
    draw.polygon(((_x, _y), (_x + _side / 2, _y + math.sqrt(3) * _side / 2), (_x + _side, _y)), fill=fill)

def polygon_equitriangle4(_x, _y, _side, draw, fill='black'):
    _x += _centre_offset_x
    _y += _centre_offset_y
    _y -= 1
    draw.polygon(((_x, _y + _side), (_x + _side / 2, _y + _side - math.sqrt(3) * _side / 2),
                  (_x + _side, _y + _side)), fill=fill)

def polygon_narrow_rectangle(_x, _y, _side, draw, fill='black'):
    _x += _centre_offset_x
    _y += _centre_offset_y
    draw.rectangle(((_x, _y + _side/4), (_x + _side-2, _y + 3 *_side / 4)), fill=fill)
    
def polygon_diamond1(_x, _y, _side, draw, fill='black'):
    _x += _centre_offset_x
    _y += _centre_offset_y
    _offset = math.sqrt(3) * _side / 2
    draw.polygon(((_x, _y + _side / 2 ), (_x + _offset / 2, _y + _side),  (_x + _offset, _y + _side / 2),
              (_x + _offset / 2, _y )), fill=fill)

def encoder(_x, _y, h, _enc_x = -4, _enc_y = 33):
    _x += _centre_offset_x
    _y += _centre_offset_y
    _x += _enc_x
    _y += _enc_y
    draw.rectangle([(_x, _y), (_x+18, _y+24)], fill=(h,h,h))

    
cmap = {'square': 0, 'equitri1': 1, 'equitri2': 2, 'equitri3': 3,
        'equitri4': 4, 'diamond1': 5}
for k in cmap:
    cmap[k] = int(cmap[k] * 255/len(cmap))

_x = 200
_y = 200

#Square
_polygon_square(_x, _y, _side, draw)
print(_x, _y, 'square')
encoder(_x, _y, cmap['square'] )

'''
_x += _x_delta
_y += _y_delta
#Circle
polygon_circle(_x, _y, _side, draw)
print(_x, _y, 'circle')
encoder(_x, _y, cmap['circle'] )
'''

_x += _x_delta
_y += _y_delta
# Equilateral triangle 1
polygon_equitriangle1(_x, _y, _side, draw)
print(_x, _y, 'equitri1')
encoder(_x, _y, cmap['equitri1'] )

_x += _x_delta
_y += _y_delta
# Equilateral triangle 2
polygon_equitriangle2(_x, _y, _side, draw)
print(_x, _y, 'equitri2')
encoder(_x, _y, cmap['equitri2'] )

_x += _x_delta
_y += _y_delta
# Equilateral triangle 3
polygon_equitriangle3(_x, _y, _side, draw)
print(_x, _y, 'equitri3')
encoder(_x, _y, cmap['equitri3'] )

_x += _x_delta
_y += _y_delta
# Equilateral triangle 4
polygon_equitriangle4(_x, _y, _side, draw)
print(_x, _y, 'equitri4')
encoder(_x, _y, cmap['equitri4'] )

'''
_x += _x_delta
_y += _y_delta
#Narrow rectangle
polygon_narrow_rectangle(_x, _y, _side, draw)
print(_x, _y, 'rect')
encoder(_x, _y, cmap['rect'] )
'''

_x += _x_delta
_y += _y_delta
# diamond 1
polygon_diamond1(_x, _y, _side, draw)
print(_x, _y, 'diamond1')
encoder(_x, _y, cmap['diamond1'] )


#Test track
_x = 200
_y = 400

# Equilateral triangle 1
polygon_equitriangle1(_x, _y, _side, draw)


_x += _x_delta
_y += _y_delta

# diamond 1
polygon_diamond1(_x, _y, _side, draw)


_x += _x_delta
_y += _y_delta

#Square
_polygon_square(_x, _y, _side, draw)


_x += _x_delta
_y += _y_delta
# Equilateral triangle 2
polygon_equitriangle2(_x, _y, _side, draw)


img.save(filename)
I(filename)
```

```python
sides = 3
_side = 100

_x = 600
_y = 500

filename = '_backgrounds/_regular_shapes.png'


# The side lengths are not right
# Ideally want to fix the origin in the centre then have all polygons inside same radius circumcircle
# Also fix rotation angle
def regular_polygon(sides, _side, _x, _y, img=None):
    """Draw a regular polygon"""
    coords = []
        
    r = (2 * math.sin(math.pi / sides )) * _side
    print(r)
    _y = _y + _side
    

    for i in range(sides):
        theta = 2 * math.pi * i / sides
        coords.append((_x + r * math.sin(theta), _y - r * math.cos(theta)))

    if not img:
        img = Image.new(mode, size, color)

    draw = ImageDraw.Draw(img)

    draw.polygon(coords, fill='black')
    
    return img

img = Image.new(mode, size, color)

img = regular_polygon(sides, _side, _x, _y, img)
img = regular_polygon(sides+1, _side, _x + 2*_side, _y, img)
img = regular_polygon(sides+2, _side, _x + 4*_side, _y, img)

img.save(filename)
I(filename)
```

```python
a = 0
b = 1
while a < 10:
    print(f'a and b incoming: {a, b}')
    a, b = b, a + b
    print(f'a and b outgoing: {a, b}')
```

## MNIST Images

To fit in a 14 x 14 grid

```python
!ls
```

```python
from IPython.display import Image as I
from PIL import Image, ImageDraw
from numpy.random import randint


filename='_backgrounds/_number_sheet.png'

mode = 'RGB'
size = (2362, 1143)
color = 'white'

from PIL import Image

#Load in the image data file
img = Image.open('mnist_batch_0.png')

import json
# The labels.txt file contains 3000 digit labels in the same order as the image data file
with open('mnist_batch_0_labels.txt', 'r') as f:
    labels = json.load(f)

# If we convert the image data to a one dimensional array (i.e. a list of values)
# the first 784 elements will represent the contents of the first row
# That is, a linear representation of the the first 28 x 28 pixel sized handwritten digit image
print(list(img.getdata())[:784])

import numpy as np

# Turn the image data into a multidimensional array
# of 3000 separate 28 x 28 arrays
images_array = np.array(img).reshape(3000, 28, 28)

#Get the third item (index value 2), that is, the third 28 x 28 image data array
image_array = images_array[2]

# And convert it to an image
image_image = Image.fromarray(image_array)

# Then display it
image_image

img = Image.new(mode, size, color)
draw = ImageDraw.Draw(img)
img_cnt = len(images_array)


_x_offset = -27
_y_offset = 6


def coded_square(draw, x, y, h, offset=10):
    """Generate a simple coded square in the centre"""
    draw.rectangle([x+offset, y+offset, x+offset+1, y+offset+1], fill=(255, 0, 0))
    draw.rectangle([x+offset+1, y+offset, x+offset+2, y+offset+1], fill=(0, 255, 0))
    draw.rectangle([x+offset, y+offset+1, x+offset+1, y+offset+2], fill=(0, 0, 255))
    draw.rectangle([x+offset+1, y+offset+1, x+offset+2, y+offset+2], fill=(255-h, 255-h, 255-h))              
    
for i in range(20):
    for j in range(20):
        _img = randint(img_cnt)
        arr = images_array[_img]
        img_N = Image.fromarray(arr.reshape(28, 28), 'L')
        img_Ns = img_N.resize((14, 14), Image.LANCZOS)
        img.paste(img_Ns, (100+_x_offset+i*100, 50+_y_offset+j*100))
        #draw.text((100+i*100, 40+j*100), str(z[_img]), fill=(0,0,0))
        
        # We can draw a square with grey scale values that encode the training set value
        _x, _y = (100+i*100, 40+j*100)
        h = labels[_img] * 25
        draw.rectangle([(_x+38+_x_offset, _y+7+_y_offset),
                        (_x+58+_x_offset, _y+30+_y_offset)], fill=(h,h,h))

        #coded_square(draw, _x+38+_x_offset, _y+7+_y_offset, h)

img.save(filename)
I(filename)
```

## Elevation and Contours


```python
#!pip install elevation
#!conda install -y  -c conda-forge gdal
#https://www.earthdatascience.org/tutorials/visualize-digital-elevation-model-contours-matplotlib/


#Maybe get topographical data for other planets, eg via recipe in:
# https://github.com/eleanorlutz/topography_atlas_of_space
```

```python
from osgeo import gdal
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import elevation 
```

```python
#!wget https://planetarymaps.usgs.gov/mosaic/Mars_MGS_MOLA_DEM_mosaic_global_463m.tif
```

```python
# GIven lat long and bounding box, find other coords
#https://stackoverflow.com/a/238558/454773
# degrees to radians
import math

def deg2rad(degrees):
    return math.pi*degrees/180.0
# radians to degrees
def rad2deg(radians):
    return 180.0*radians/math.pi

# Semi-axes of WGS-84 geoidal reference
WGS84_a = 6378137.0  # Major semiaxis [m]
WGS84_b = 6356752.3  # Minor semiaxis [m]

# Earth radius at a given latitude, according to the WGS-84 ellipsoid [m]
def WGS84EarthRadius(lat):
    # http://en.wikipedia.org/wiki/Earth_radius
    An = WGS84_a*WGS84_a * math.cos(lat)
    Bn = WGS84_b*WGS84_b * math.sin(lat)
    Ad = WGS84_a * math.cos(lat)
    Bd = WGS84_b * math.sin(lat)
    return math.sqrt( (An*An + Bn*Bn)/(Ad*Ad + Bd*Bd) )

# Bounding box surrounding the point at given coordinates,
# assuming local approximation of Earth surface as a sphere
# of radius given by WGS84
def boundingBox(latitudeInDegrees, longitudeInDegrees, halfSideInM_x, halfSideInM_y):
    lat = deg2rad(latitudeInDegrees)
    lon = deg2rad(longitudeInDegrees)

    # Radius of Earth at given latitude
    radius = WGS84EarthRadius(lat)
    # Radius of the parallel at given latitude
    pradius = radius*math.cos(lat)

    latMin = lat - halfSideInM_y/radius
    latMax = lat + halfSideInM_y/radius
    lonMin = lon - halfSideInM_x/pradius
    lonMax = lon + halfSideInM_x/pradius

    return (rad2deg(latMin), rad2deg(lonMin), rad2deg(latMax), rad2deg(lonMax))


a, b, c, d = boundingBox(40.5, -121.5, size[0]*10, size[1]*20)

cc = f'{b} {a} {d} {c}'
cc
```

```python
# Data from NASA's Shuttle Radar Topography Mission 
# latitude 41.15 and longitude -122.6, near Mt. Shasta in North California


#!eio clip -o Shasta-30m-DEM.tif --bounds -123 41 -122 42 
!eio clip -o Shasta-30m-DEM.tif --bounds $cc
```

```python
!gdaldem color-relief jotunheimen.tif 
```

```python
filename = "Shasta-30m-DEM.tif"
gdal_data = gdal.Open(filename)
gdal_band = gdal_data.GetRasterBand(1)
nodataval = gdal_band.GetNoDataValue()

# convert to a numpy array
data_array = gdal_data.ReadAsArray().astype(np.float)
data_array

# replace missing values if necessary
if np.any(data_array == nodataval):
    data_array[data_array == nodataval] = np.nan
```

```python
#Plot our data with Matplotlib's 'contourf'
size = (2362, 1143)

#https://stackoverflow.com/a/13714720/454773

#fig = plt.figure(figsize=(size[0]/100, size[1]/100), dpi=100)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.contourf(data_array, cmap = "magma", # inferno, viridis, plasma, magma, cividis
            levels = list(range(0, 5000, 100)))
#plt.title("Elevation Contours of Mt. Shasta")
#cbar = plt.colorbar()
plt.gca()#.set_aspect('equal', adjustable='box')
plt.axis('off')
print(fig.get_size_inches()*fig.dpi)
fig.set_size_inches((size[0]/100, size[1]/100))
plt.savefig('Topo_map.png', dpi=100)
plt.show()
```

```python
2362/ 1143, 432./ 288.
```

### Raster Lidar

```python
#%pip install rasterio
#%pip install shapely
#%pip install earthpy
```

```python
#https://www.earthdatascience.org/workshops/gis-open-source-python/open-lidar-raster-python/

import os
import numpy as np
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import show
from rasterio.plot import show_hist
from shapely.geometry import Polygon, mapping
from rasterio.mask import mask

import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

# set home directory and download data
et.data.get_data("spatial-vector-lidar")
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))

```

```python
!ls data/spatial-vector-lidar/california/neon-soap-site/2013/lidar
```

```python
# define path to digital terrain model
sjer_dtm_path = "data/spatial-vector-lidar/california/neon-soap-site/2013/lidar/SOAP_lidarDTM.tif"
#sjer_dtm_path = "notebooks/content/uk_lidar_test.tif"
# open raster data
lidar_dem = rio.open(sjer_dtm_path)
# optional - view spatial extent
lidar_dem.bounds
```

```python
!pwd
```

```python
# plot the dem using raster.io
fig, ax = plt.subplots(figsize=(size[0]/100, size[1]/100), dpi=100)
show(lidar_dem, 
     title="Lidar Digital Elevation Model (DEM) \n Boulder Flood 2013", 
     ax=ax, cmap='magma')

ax.set_axis_off()
plt.savefig("test_lidar.png",bbox_inches='tight',dpi=100)
```

```python
# defra lidar
#https://www.roger-pearse.com/weblog/2019/07/08/tutorial-how-to-download-the-lidar-datasets-from-the-uk-environment-agency-website/comment-page-1/
%cd ~
!ls notebooks/content/LIDAR-DSM-2M-SZ68nw/
```

```python
!ls
```

```python
#https://gis.stackexchange.com/a/169494
!gdal_translate notebooks/content/LIDAR-DSM-2M-SZ68nw/sz6187_DSM_2M.asc notebooks/content/uk_lidar_test.tif
```

## Block diag


## Flow charts

The nicest flow charts are probably produced using tikz and LateX or graphviz, but that it perhaps overkill. Mermaind.js works okay, but the diagrams are a bit ropey. drawi.io can also be used to draw flowcharts, but I don't think they can be scripted? [flowchart.js](https://github.com/adrai/flowchart.js) looks interesting: can we perhaps create a magic for that?

```python
import jp_proxy_widget
```

```python
fcode = '''
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End|future:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes
or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|future

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->sub1(left)->op1
c2(yes)->io->e
c2(no)->op2->e
'''
```

```python


fcode = '''
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End|future:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes
or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|future

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->sub1(left)->op1
c2(yes)->io->e
c2(no)->op2->e
'''
fcode='''
st=>start: Start
e=>end: End
op1=>operation: Generate
op2=>parallel: Evaluate
st(right)->op1(right)->op2
op2(path1, top)->op1
op2(path2, right)->e
'''
import jp_proxy_widget
import uuid
from IPython.display import Image, SVG
import cairosvg

class FlowchartWidget(jp_proxy_widget.JSProxyWidget):
    """jp_proxy_widget to render flowchart.js diagrams."""
    def __init__(self, *pargs, **kwargs):
        super(FlowchartWidget, self).__init__(*pargs, **kwargs)
        e = self.element
        e.empty()
        self.load_js_files(["https://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js",
                            'https://cdnjs.cloudflare.com/ajax/libs/flowchart/1.13.0/flowchart.js'])
        self.uid = None
        self.svg = None

    def charter(self, chart, embed=False):
        """Render chart from chart description."""
        self.uid = uid = uuid.uuid4()
        self.element.html(f'<div id="{uid}"></div>')
        self.set_element("chartdef", chart)
        self.js_init(f"chart = flowchart.parse(element.chartdef); chart.drawSVG('{uid}');svg_data = document.getElementById('{uid}').innerHTML;")
        self.get_value_async(self.svg_callback, "svg_data")
        if embed:
            return self

    def svg_callback(self, svg):
        """Persist SVG state on Python side."""
        self.svg = svg
    
    def get_svg_data(self):
        """Return raw SVG data for flowchart."""
        return self.svg
    
    def get_svg(self):
        """Return SVG data of flowchart."""
        return SVG(self.svg)
    
    def get_png(self):
        """Return png of flowchart."""
        return Image(cairosvg.svg2png(self.svg));
 
    
testEmbed = FlowchartWidget()
testEmbed.charter(fcode)
testEmbed

#testEmbed.get_svg_data()
#testEmbed.get_svg()
#testEmbed.get_png()
```

```python
fw = FlowchartWidget()
fw.charter('''
st=>start: Start
e=>end: End
op1=>operation: Generate
op2=>parallel: Evaluate
st(right)->op1(right)->op2
op2(path1, top)->op1
op2(path2, right)->e
''')
fw
```

```python
import time
time.sleep?
```

```python
import time time.sleep
```

```python
testEmbed.get_svg()
```

```python
testEmbed.get_svg_data()
```

```python
testEmbed.get_png()
```

```python
FlowchartWidget().charter(fcode, embed=True)
```

## Graphviz - NN diagrams

eg http://webgraphviz.com/

<!-- #region -->
#Based on https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/

digraph G {

        rankdir=LR
	splines=line
        

        subgraph cluster_0 {
		color=white;
		node [style=solid,color=blue4, shape=circle];
		x1 x2;
		label = "Input layer";
	}

	subgraph cluster_1 {
		color=lightgrey;
		style=filled;
		node [style=solid,color=black, shape=circle];
		a12 a22 a32;
		label = "Hidden layer)";

	}



	subgraph cluster_2 {
		color=white;
		node [style=solid, shape=circle];
		O1 O2 O3 O4;
		label="Output layer";
	}

        x1 -> a12;
        x1 -> a22;
        x1 -> a32;
        x2 -> a12;
        x2 -> a22;
        x2 -> a32;


        a12 -> O1;
        a22 -> O1;
        a32 -> O1;

        a12 -> O2;
        a22 -> O2;
        a32 -> O2;

        a12 -> O3;
        a22 -> O3;
        a32 -> O3;

        a12 -> O4;
        a22 -> O4;
        a32 -> O4;

        x -> x1[dir=none color="black"];
        x [label="x", color="white"];
        y -> x2[dir=none color="black"];
        y [label="y", color="white"];

        O1 -> P[dir=none color="black"];
        P [label="Pear", color="white"];
        O2 -> B[dir=none color="black"];
        B [label="Banana", color="white"];
        O3 -> S[dir=none color="black"];
        S [label="Strawberry", color="white", fontsize=12];
        O4 -> O[dir=none color="black"];
        O [label="Orange", color="white"];
        
}
<!-- #endregion -->

## Tones

Example tones for use as various audio cues.

```python
from IPython.display import Javascript
```

```python
#https://marcgg.com/blog/2016/11/01/javascript-audio/
js = '''
function example4(frequency, type) {
    o = context.createOscillator()
    g = context.createGain()
    o.type = type
    o.connect(g)
    o.frequency.value = frequency
    g.connect(context.destination)
    o.start(0)
    g.gain.exponentialRampToValueAtTime(0.00001, context.currentTime + 1)
}
'''

display(Javascript(tone+"example4(440, 'square')"))
```

```python
#via ??

## See also:
# https://marcgg.com/blog/2016/11/01/javascript-audio/
# https://css-tricks.com/introduction-web-audio-api/

tone='''
var context = new AudioContext()
var o = null
var g = null
document.addEventListener('DOMContentLoaded', function() {
    $(".js_play_sound").on("click", function(e) {
        e.preventDefault()
        var $target = $(e.target)
        eval($target.data("source"))
    })
    $(".js_stop_sound").on("click", function(e) {
        e.preventDefault()
        o.stop()
    })
}, false)

function example1() {
    o = context.createOscillator()
    o.type = "sine"
    o.connect(context.destination)
    o.start()
}

function example2() {
    o = context.createOscillator()
    g = context.createGain()
    o.connect(g)
    g.connect(context.destination)
    o.start(0)
}

function example2Stop(decreaseTime) {
    g.gain.exponentialRampToValueAtTime(0.00001, context.currentTime + decreaseTime)
}

function example3(type, x) {
    o = context.createOscillator()
    g = context.createGain()
    o.connect(g)
    o.type = type
    g.connect(context.destination)
    o.start(0)
    g.gain.exponentialRampToValueAtTime(0.00001, context.currentTime + x)
}

function example4(frequency, type) {
    o = context.createOscillator()
    g = context.createGain()
    o.type = type
    o.connect(g)
    o.frequency.value = frequency
    g.connect(context.destination)
    o.start(0)
    g.gain.exponentialRampToValueAtTime(0.00001, context.currentTime + 1)
}
'''
```

```python
from IPython.display import Javascript
Javascript(tone+"example3('sine', 0.005)")
```

```python
# Bright success?
Javascript(tone+"example3('square', 1.5)")
```

```python
# Deeper fail?
Javascript(tone+"example4('50', 'sawtooth')")
```

## ChatBot Scripts

```python
from chatterbot import ChatBot
chatbot = ChatBot("Test")
from IPython.display import clear_output
clear_output()
```

```python
print(chatbot.get_response("Good morning!"))

```

```python
print(chatbot.get_response("How are you today?"))
```

```python
from chatterbot.trainers import ListTrainer
```

```python
ChatBot?
```

```python
chatbot = ChatBot('as');
```

```python
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
]
)

trainer.train([
    "Hello",
    "What time is it in France",
    "Quarter past twelve."
    "Is that the time?"
])

trainer.train([
    "Morning",
    "What time is it in Germany",
    "get a flight."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Can I get a flight to Iceland?')

print(response)
```

## Explorables



```python
%%HTML
<script src="https://unpkg.com/@iooxa/components"></script>
<div style="display: none;">
<r-var name="cookies" value="3" format=".4"></r-var>
<r-var name="caloriesPerCookie" value="50"></r-var>
<r-var name="dailyCalories" value="2100"></r-var>

<r-var name="calories" :value="cookies * caloriesPerCookie" format=".0f"></r-var>
<r-var name="dailyPercent" :value="calories / dailyCalories" format=".0%"></r-var>
</div>
<p>
  When you eat <r-dynamic bind="cookies" min="2" max="100">cookies</r-dynamic>,
  you consume <r-display bind="calories"></r-display> calories.<br>
  That's <r-display bind="dailyPercent"></r-display> of your recommended daily calories.
</p>
```

## Show Diff

```python
#https://github.com/dsindex/blog/wiki/%5Bpython%5D-difflib,-show-differences-between-two-strings
import difflib
from IPython.display import HTML

def show_diff(text, n_text, retval=False):
    """
    Display the difference between two strings.
    http://stackoverflow.com/a/788780
    Unify operations between two compared strings seqm is a difflib.
    SequenceMatcher instance whose a & b are strings
    """
    seqm = difflib.SequenceMatcher(None, text, n_text)
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':
            output.append("<font color=red>^" + seqm.b[b0:b1] + "</font>")
        elif opcode == 'delete':
            output.append("<font color=blue>^" + seqm.a[a0:a1] + "</font>")
        elif opcode == 'replace':
            # seqm.a[a0:a1] -> seqm.b[b0:b1]
            output.append("<font color=green>^" + seqm.b[b0:b1] + "</font>")
        output.append('<br/>')
    txt=''.join(output)
    
    if retval: return txt
    return HTML('<pre>'+txt+'</pre>')
```

```python
show_diff('some text!', 'Some text')
```

```python
#https://stackoverflow.com/a/788780/454773
def show_diff2(seqm):
    """Unify operations between two compared strings
seqm is a difflib.SequenceMatcher instance whose a & b are strings"""
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':
            output.append("<ins>" + seqm.b[b0:b1] + "</ins>")
        elif opcode == 'delete':
            output.append("<del>" + seqm.a[a0:a1] + "</del>")
        elif opcode == 'replace':
            raise NotImplementedError("what to do with 'replace' opcode?")
        else:
            raise RuntimeError("unexpected opcode")
    return ''.join(output)

sm= difflib.SequenceMatcher(None, "lorem ipsum dolor sit amet", "lorem foo ipsem dolor amet;")
show_diff2(sm)
# So use spand and class tags and colour highlight with css?
```

```python pinned_outputs=[]
#https://stackoverflow.com/a/47617607/454773
def inline_diff(a, b):
    import difflib
    matcher = difflib.SequenceMatcher(None, a, b)
    def process_tag(tag, i1, i2, j1, j2):
        if tag == 'replace':
            return '{' + matcher.a[i1:i2] + ' -> ' + matcher.b[j1:j2] + '}'
        if tag == 'delete':
            return '{- ' + matcher.a[i1:i2] + '}'
        if tag == 'equal':
            return matcher.a[i1:i2]
        if tag == 'insert':
            return '{+ ' + matcher.b[j1:j2] + '}'
        assert False, "Unknown tag %r"%tag
    return ''.join(process_tag(*t) for t in matcher.get_opcodes())
a ='Lorem ipsum dolor sit amet consectetur adipiscing'
b='Lorem bananas ipsum cabbage sit amet adipiscing'
inline_diff(a, b)

```

We can access the contents of code cell that has been executed given its IPython execution index number. Using this number to reference the cell history —  `_ih[CELL_INDEX]` — gives us a copy of the cell content.

```python
_ih[168]
```

```python code_folding=[0]
#Google differ - this is pretty
#https://github.com/google/diff-match-patch
```

```python
d = diff_match_patch()
```

```python
d.diff_main('this sentence', 'that sentence;')
```

```python
HTML(d.diff_prettyHtml(d.diff_main('this sentence', 'that sentence;')))
```

The Google differ is available in python and javascript; would be interesting to be able to tag two related cells and as a toggle view highlight the second one showing a diff from the first.

Can we easily display the difference between the contents of two code cells?

```python
#https://github.com/google/diff-match-patch
import sys
sys.path.insert(0,'..')

from diff_match_patch import diff_match_patch
differ = diff_match_patch()
```

```python
# SOme code
print('hello')
print('goodbye')
```

```python
# Some code
print('hello, there')
print('goodbye')
```

```python
HTML(differ.diff_prettyHtml(differ.diff_main(_ih[179], _ih[180])))
```

```python
!conda info --envs
```

## Display Handles

https://mindtrove.info/jupyter-tidbit-display-handles/

```python
from IPython.display import Markdown
dh = display(display_id=True)
dh.display(Markdown('sss'))
```

```python
 dh.update(Markdown('updatsdsdsedasa2'))
```

```python
dh = display(display_id=True)
display(Markdown('# Display Update Fun'))
dh.display(Markdown('sss'))
```

```python
dh.update(Markdown('# Display Update FUn3'));
```

```python
dh.update(Markdown('# Display Update FUn4'));
```

## MArkdown Images

GEnerate metadata for markdown images:

```python
#%pip install beautifulsoup4
#%pip install Markdown
##%pip install markdown-image-caption
```

```python
import markdown


%cd ~/notebooks
txt = open('seminar_tm129_robotics_overview.md', 'r').read()
html = markdown.markdown(txt)#,extensions=["markdown_image_caption.plugin"])


from bs4 import BeautifulSoup

soup = BeautifulSoup(html)
for imgtag in soup.find_all('img'):
    print(imgtag['src'],imgtag['alt'])

```

```python
html

```

# Audio

```python
from IPython.display import Javascript
```

```python
from IPython.display import Audio, Javascript

display(
            Javascript(
                """var beep = (function () {
    var ctxClass = window.audioContext ||window.AudioContext || window.AudioContext || window.webkitAudioContext
    var ctx = new ctxClass();
    return function (duration, type, finishedCallback) {

        duration = +duration;

        // Only 0-4 are valid types.
        type = (type % 5) || 0;

        if (typeof finishedCallback != "function") {
            finishedCallback = function () {};
        }

        var osc = ctx.createOscillator();

        osc.type = type;
        //osc.type = "sine";

        osc.connect(ctx.destination);
        if (osc.noteOn) osc.noteOn(0); // old browsers
        if (osc.start) osc.start(); // new browsers

        setTimeout(function () {
            if (osc.noteOff) osc.noteOff(0); // old browsers
            if (osc.stop) osc.stop(); // new browsers
            finishedCallback();
        }, duration);

    };
})(); beep();"""))
```

```python
from IPython.display import Javascript

def say(txt):
        """Speak an utterance."""
        js = f'''
        var utterance = new SpeechSynthesisUtterance("{txt}");
        '''
        js = js + 'speechSynthesis.speak(utterance);'
        display(Javascript(js))
say('All done')
```

```python
say('All done')
```

```python
#via https://github.com/tqdm/tqdm/issues/988
from tqdm.notebook import tqdm as tqdm_notebook_orig
from tqdm.notebook import tqdm

class tqdm_notebook(tqdm_notebook_orig):
    def close(self, *args, **kwargs):
        if self.disable:
            return
        super(tqdm_notebook, self).close(*args, **kwargs)

        from IPython.display import Javascript, display
        display(Javascript('''
        var ctx = new AudioContext()
        function tone(duration=1.5, frequency=400, type='sin'){
          var o = ctx.createOscillator(); var g = ctx.createGain()
          o.frequency.value = frequency; o.type = type
          o.connect(g); g.connect(ctx.destination)
          o.start(0)
          g.gain.exponentialRampToValueAtTime(0.00001, ctx.currentTime + duration)
        }
        tone(1.5, 600)'''))
        
tqdma = tqdm_notebook
```

```python
import time
for i in tqdm(range(10), ):
    time.sleep(0.1)
for i in tqdma(range(10), ):
    time.slep(0.1)

```

```python

```
