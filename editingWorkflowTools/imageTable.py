# # Image Table
#
# Script to generate a gallery table showing images used in documents by folder.
#
# Table structure:
#
# - path
# - directory
# - file
# - img_path
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

# First, let's create a function that will generate a list of images from a markdown file, given the path to the markdown file.
#
# Images in markdown are encoded as `![ALT_TEXT](IMAGE_FILEPATH)` or explicilty in HTML `<img />` tags. Either way, we should be able to parse them out because the approach I'm taking is to parse the markdown to HTML, then extract the `img` tags.
#
# The function will return a list of two tuples containing the image path and any alt text.

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

The next step is to iterate through a set of files

# +
import os

def parse_file_collection(rootdir='.'):
    """Parse all the markdown files in all the subdirs of a specified directory."""
    biglist = []
    for subdir, dirs, files in os.walk(rootdir):
        if '.ipynb_checkpoints' in subdir:
            continue
        for file in [f for f in files if f.endswith('md')]:
            fpath = os.path.join(subdir, file)
            _images = get_images_from_md(fpath)
            for (src, alt) in _images:
                if alt:
                    print(alt)
                img_path = os.path.join(subdir, src)
                biglist.append([alt, f'![{alt}]({img_path})', img_path.replace(rootdir, ''),
                                subdir, file, f'[{fpath}]({fpath})'])
    return biglist


# +
rootdir = '../content'

biglist = parse_file_collection(rootdir)
biglist[:2]


# -

def write_gallery_file(biglist, outfilepath='gallery.md', headers=None, typ='github' ):
    """Generate a gallery file."""
    with open(outfilepath, 'w') as f:
        f.write(tabulate(biglist, headers=headers, tablefmt=typ))


headers = ['Alt text', 'Image', 'Image Path', 'Path', 'Directory', 'Filename']
write_gallery_file(biglist, headers=headers)

# !head gallery.md


