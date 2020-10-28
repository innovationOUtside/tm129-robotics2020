---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Reproducible Diagrams

This notebook contains various source scripts for diagrams used in the teaching materials.

- https://github.com/uclnlp/egal
- https://github.com/cduck/drawSvg

Draw.io


## Code 2 simulator and robot

```python
#https://github.com/cduck/drawSvg
import drawSvg as draw

d = draw.Drawing(200, 100, origin='center', displayInline=False)

d.append(draw.Rectangle(0, 0, 40, 50, fill='#ffffff', stroke='black'))

d.append(draw.Text('Hyperlink', 20, 0,0, fill='black'))
d
```

```python
draw.Lines(0, -45,
                    70, -49,
                    95, 49,
                    -90, 40,
                    close=False,
            fill='#eeee00',
            stroke='black'))
```
