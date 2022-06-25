# mpl_fontkit

- Use font from google fonts
- Set the font and use it easily

### Install

```shell
pip install mpl_fontkit
```

### Quick Start

```python
from mpl_fontkit import FontKit

# https://fonts.google.com/specimen/Lato?query=Lato
fk = FontKit().get("Lato")
# To check available styles for the font
fk.font_table("Lato")
```
```shell
  Name     Style    Variant    Weight   Stretch 
  ----     -----    -------    -----    ------- 
  Lato     normal    normal     250      normal 
  Lato     italic    normal     250      normal 
  Lato     normal    normal     300      normal 
  Lato     italic    normal     300      normal 
  Lato     normal    normal     400      normal 
  Lato     italic    normal     400      normal 
  Lato     normal    normal     700      normal 
  Lato     italic    normal     700      normal 
  Lato     normal    normal     900      normal 
  Lato     italic    normal     900      normal 
```

And then you are ready to use it in your plots

```python
import matplotlib.pyplot as plt
_, ax = plt.subplots()
ax.set_title("Lato Font", fontdict={"style": "italic", 
                                    "weight": 700, 
                                    "size": 24})
```
<img src="images/in_plot.svg" alt="show in plot" width="300">

#### Get usable fonts

```python
from mpl_fontkit import FontKit
print(FontKit().fonts())
```
```shell
['Agency FB',
 'Algerian',
 'Arial',
 'Arial Rounded MT Bold',
 'Bahnschrift',
 'Baskerville Old Face',
 'Bauhaus 93',
 ...]
 
 ```

### To show what a font looks like
```python
from mpl_fontkit import FontKit
FontKit().show("Lato")
# To display all fonts at once
# FontKit().show_fonts()
```
<img src="images/show.svg" width="300">

