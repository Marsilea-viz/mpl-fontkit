# mpl_fontkit

![pypi](https://flat.badgen.net/pypi/v/mpl_fontkit?color=blue)

- Use font from google fonts
- Set the font and use it easily
- Helpful error message to get your font name right

### Install

```shell
pip install mpl_fontkit
```

### Quick Start

```python
from mpl_fontkit import FontKit

# https://fonts.google.com/specimen/Lato?query=Lato
fk = FontKit().get("Lato")
```
If the font does not available in matplotlib,
this will download from Google and add it to
matplotlib.

To check available styles for a font
```python
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
<img src="https://raw.githubusercontent.com/Mr-Milk/mpl-fontkit/main/images/in_plot.svg" alt="show in plot" width="300">

To set a font manually. 
This will update the `rcParams` for you.
```python
from mpl_fontkit import FontKit
FontKit().set_global("Lato")
```

Most of the time when you can't get the font to work
simply because the font name is not the same as the file name.
You can just type a fuzzy name, we will try to find
a similar name and show you in the error message.

```python
from mpl_fontkit import FontKit
FontKit().set_global("Lat")
```
```shell
LookupError: Cannot find Lat, do you mean: Lato. Use `.fonts()` to list all the available fonts.
```

#### Get available fonts

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
<img src="https://raw.githubusercontent.com/Mr-Milk/mpl-fontkit/main/images/show.svg" width="300">

