# # Image Table
#
# Script to generate a gallery table showing images used in documents by folder.
#
# Table structure:
#
# - path
# - directory
# - file
# - alt text
# - image

#https://github.com/astanin/python-tabulate
# #%pip install tabulate
from tabulate import tabulate

# ## Recipe
#
# - iterate through subdirs of specified path
# - grab markdown files in subdir
# - generate table from images in markdown file

# +
import markdown
from bs4 import BeautifulSoup

def get_images_from_md(fpath):
    """Get images from file."""
    images = []
    txt = open(fpath, 'r').read()
    html = markdown.markdown(txt)#,extensions=["markdown_image_caption.plugin"])
    soup = BeautifulSoup(html)
    for imgtag in soup.find_all('img'):
        if 'alt' not in imgtag:
            imgtag['alt'] = ''
        images.append((imgtag['src'], imgtag['alt']))
    return images


# -

# !ls ../content/01_Robot_Lab

# +
import os
rootdir = '../content'

biglist = []
for subdir, dirs, files in os.walk(rootdir):
    for file in [f for f in files if f.endswith('md')]:
        fpath = os.path.join(subdir, file)
        _images = get_images_from_md(fpath)
        for (src, alt) in _images:
            biglist.append([subdir, file, f'[{fpath}]({fpath})', alt, f'![{alt}]({os.path.join(subdir, src)})'])
# -

biglist[:2]

with open('gallery.md', 'w') as f:
    f.write(tabulate(biglist,
                     headers=['Path', 'Directory', 'Filename', 'Alt text', 'Image'],
                     tablefmt='github'))

# !head gallery.md

# !ls ..


