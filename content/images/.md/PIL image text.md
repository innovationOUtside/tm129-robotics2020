---
jupyter:
  jupytext:
    formats: ipynb,.md//md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
from PIL import Image, ImageDraw, ImageFont
```

```python
!ls /usr/share/fonts/truetype/dejavu/
```

```python
im = Image.open('SS9_car_305_top_40.png')
position = (100, 100)
text = "Explanatory text"
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', 64)
color = (0, 0, 0)
```

```python

# get text size
text_size = font.getsize(text)

# initialise the drawing context with the image object as background
draw = ImageDraw.Draw(im)


draw.rectangle([position, (position[0]+text_size[0]+10,position[1]+text_size[1]+10)], fill='orange', outline='orange', width=5)
draw.text(position, text, fill=color, font=font)
draw.line([(0,0),position], fill='red', width=5)
im
```

The following will load in the matplotlib interactive backend, then when you hove the cursor over the image, it will show the current co-ordinates.

```python
%matplotlib notebook
import matplotlib.pyplot as plt

plt.imshow(im)
```

```python
#https://stackoverflow.com/a/52574134/454773
coords = None

%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as wdg  # Using the ipython notebook widgets

fig = plt.figure()
plt.imshow(im)

# Create and display textarea widget
txt = wdg.Textarea(
    value='',
    placeholder='',
    description='Co-ords:',
    disabled=False
)
display(txt)

# Define a callback function that will update the textarea
def onclick(event):
    global coords
    coords=event
    txt.value = f'{coords.x}, {coords.y}'  # Dynamically update the text box above

# Create an hard reference to the callback not to be cleared by the garbage collector
ka = fig.canvas.mpl_connect('button_press_event', onclick)
```

```python
coords.x, coords.y
```

```python
dir(coords)
```

```python
#im.show()
```

```python
image_name_output = '03_add_text_to_image_02_input_01.jpg'
im.save(image_path_output + image_name_output)
```

```python
%matplotlib inline
```

```python

```
