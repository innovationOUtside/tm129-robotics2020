# -*- coding: utf-8 -*-
# # Editor Pass
#
# Routines based on changed suggested by editor to original material.

# ## Style guide
#
# Style guide items, including:
#     
# - sentence case for headings
# - *program* NOT *programme*
# - *Markdown* NOT *markdown*
# - *RoboLab* NOT *RobotLab* unless we actually refer to original RobotLab?)
#
#
#

word_replacement = {
    r"\b([Pp]+)rogramme\b": r"\1rogram"
}
case_replacement = {
    r"\b([Pp]+)rogramme\b": r"\1rogram",
    'markdown': 'Markdown',
    'RobotLab': 'RoboLab',
    'RoboLab': 'RoboLab'
}

# Constraints:
#
#     - word replacement should preserve the case of the first letter;
#     - we shouldn't break things through stemming (eg *programmer* should not be changed to *programer*);

import re
re.sub(r"\b([Pp]+)rogramme\b", r"\1rogram", "The programme? It was a programme programmed by a programmer, and we called it 'The Programme'")


def process_typos(txt, replacer, case):
    """Replace typos."""
    for k, v in replacer.items():
        txt = re.sub(k, v, txt)
    for k, v in case.items():
        txt = re.sub(k, v, txt, flags=re.IGNORECASE)
    return txt


# +
s = '''
This text has the word markdown in it and the word RobotLab.
The programme? It was a programme programmed by a programmer, and we called it 'The Programme'.
'''

print(process_typos(s, word_replacement))
# -

# ## Headers
#
# Some routines for cleaning headers

# Replace dash in title
re.sub(r" - ", r" —  ", "# The dash - is not liked")


def process_headers(txt, case='sentenceCase'):
    """Get headers"""

    in_code_block = False

    #Markdown processor ignores whitespace at start and end of a markdown cell
    #txt = txt.strip()
    newtxt = []
    #We will see how to improve the handling of code blocks in markdown cells later
    for l in txt.split('\n'):
        if l.strip().startswith('```'):
            in_code_block = not in_code_block
        elif not in_code_block and l.startswith('#'):
            l = re.sub('Activity:', 'Activity —', l, flags=re.IGNORECASE)
            #Markdown heading
            # recast
            # TO DO - Where am I? gets cast as Where am i?
            if case == 'sentenceCase':
                parts = l.split()
                if len(parts)>1:
                    # TO DO - we SHOULD NOT change case of things in backquotes
                    # eg we should not change `MoveSteering` to `movestreering`
                    if not parts[1].strip()[0].isdigit():
                        parts = [parts[0]] + ' '.join(parts[1:]).capitalize().split()
                    else:
                        parts = [parts[0], parts[1]] + ' '.join(parts[2:]).capitalize().split()
                    l = ' '.join(parts)
                    # Replace dash with em-dash
                    l = re.sub(r" - ", r" —  ", l)
                parts = l.split('—')
                #if len(parts)>1:
                #    parts = [parts[0].capitalize()] + ' '.join(parts[1:]).capitalize().split()
                #    l = '–'.join(parts)
        
        newtxt.append(l)
    return '\n'.join(newtxt)


s='''# this is a Title
Here is some text.

```
# SOME CODE
sdsd
```

## Another Title

And Some Text.
'''
print(process_headers(s))

# ## Process Files

# +
import os

def _dir_file_handler(path, _f, filetype='.md'):
    """Get the filename for a single file on a specified path."""
    f = os.path.join(path, _f)
    if f.endswith(filetype):
        return f
    return None

def _dir_handler(path):
    """Handle all the notebooks in a specific directory."""
    filelist=[]
    for _f in os.listdir(path):
        fn = _dir_file_handler(path, _f)
        if fn:
            filelist.append(fn)
    return filelist
# -



# +
path='../content/05_Robot_Lab'

for fn in _dir_handler(path):
    # Read file
    with open(fn, 'r') as f:
        # Process File
        txt = f.read()
        txt = process_headers(txt)
        txt = process_typos(txt, word_replacement, case_replacement)
        

    with open(fn, 'w') as f:
        # Write File
        f.write(txt)
# -


