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
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```

<!-- #region activity=true -->
# 7 Optional extra - handling images


One of the advantages of using the Python `PIL` package is that a range of *methods* (that is, *functions*) are defined on each image object that allow us to manipulate it *as an image*. (We can then also access the data defining the transformed image *as data* if we need it in that format.)

We can preview the area in our sampled image by cropping the image to the area of interest:

```python
# The crop area is (x, y, x + side, y + side)
cropped_image = img.crop((3, 3, 17, 17));
                       
display(cropped_image.size)
zoom_img(cropped_image)
```

In order to present this image as a test image to the trained MLP, we need to resize it so that it is the same size as the training images:

```python
from PIL import Image

# TO DO - should we add crop and resize as parameters to generate_image?
resized_cropped_image = cropped_image.resize((28, 28), Image.LANCZOS)
zoom_img(resized_cropped_image)
```

```python
generate_image(roboSim.image_data(), index,
               crop=(3, 3, 17, 17),
               resize=(28, 28))
```

```python
image_class_predictor(MLP, resized_cropped_image);
```

```python
The `sensor_data.sensor_image_focus()` function will take an image, crop it to the central area, a
```


## Playing with images

If we create a blank image of size 28x28 pixels with a grey background, we can paste a copy of our cropped image into it.
 
```python
_grey_background = 200

_image_size = (28, 28)
_image_mode = 'L' #greyscale image mode

shift_image = Image.new(_image_mode, _image_size, _grey_background)

# Set an offset for where to paste the image
_xy_offset = (2, 6)

shift_image.paste(cropped_image, _xy_offset) 
zoom_img(shift_image)
```

Alternatively, we might zoom the cropped image back to the original image size. (The `Image.LANCZOS` setting defines a filter that is used to interpolate new pixel values in the scaled image based on the pixel values in the cropped image. As such, it may introduce digital artefacts of its own into the scaled image.)

```python
resized_image = cropped_image.resize(image_image.size, Image.LANCZOS)

display( resized_image.size)
zoom_img(resized_image)
```


Note that other image handling tools are available to us within the `PIL` package that allow us to perform other "native" image manipulating functions, such as cropping an image:

```python
# Define the limits of the crop operation

# Cut 6 pixel columns on lefthand edge
x0 = 6
# Cut 10 pixel columns on righthand edge
x1 = image_image.size[1] -10

# Leave the rows alone
y0 = 0
y1 = image_image.size[1]

crop_image = image_image.crop((x0, y0, x1, y1))
zoom_img(crop_image)
```
<!-- #endregion -->
