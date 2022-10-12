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
import mpl_fontkit as fk

# https://fonts.google.com/specimen/Lato?query=Lato
fk.install("Lato")
```
If the font does not available in matplotlib,
this will download from Google and add it to
matplotlib.

To check available styles for a font
```python
fk.font_table("Lato")
```
<img src="https://raw.githubusercontent.com/Mr-Milk/mpl-fontkit/main/images/font_table.svg" width="300">

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
import mpl_fontkit as fk

fk.set_font("Lato")
```

Most of the time when you can't get the font to work
simply because the font name is not the same as the file name.
You can just type a fuzzy name, we will try to find
a similar name and show you in the error message.

```python
import mpl_fontkit as fk

fk.set_font("Lat")
```
```text
LookupError: Cannot find Lat, do you mean: Lato. 
    Use `.list_fonts()` to list all the available fonts.
```

#### Get available fonts

```python
fk.list_fonts()
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

### What fonts look like?

Show one font
```python
fk.show("Lato")
```
<img src="https://raw.githubusercontent.com/Mr-Milk/mpl-fontkit/main/images/show.svg" width="300">

Show all fonts at once
```python
fk.show_fonts()
```