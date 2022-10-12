import shutil
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import fontManager
from rich.console import Console
from rich.table import Table
from thefuzz import fuzz
from thefuzz import process

from mpl_fontkit.download import get_google_font


def _get_current_fonts_name():
    return set([font.name for font in fontManager.ttflist])


def _get_similar_font(font):
    result, _ = process.extractOne(font,
                                   _get_current_fonts_name(),
                                   scorer=fuzz.token_sort_ratio)
    return result


def _raise_font_no_exist(font):
    similar = _get_similar_font(font)
    error_msg = f"Cannot find {font}, do you mean: {similar}. " \
                f"Use `.list_fonts()` to list all the available fonts."
    raise LookupError(error_msg)


def _has_font(font):
    return font in _get_current_fonts_name()


def get_font_install_path():
    install_path = Path(".fonts")
    install_path.mkdir(exist_ok=True)
    return install_path


def clean():
    p = get_font_install_path()
    shutil.rmtree(p)


def install(
        font,
        as_global=True,
        save=None,
        source="google",
        use_cache=True):
    """To get a font from other resources

    Args:
        font: The name of the font family
        as_global: Set this font the default for matplotlib
        save: The path to save the font files
        source: 'google'
        use_cache: Use local cached font files or download again

    Returns:

    """
    if not _has_font(font):
        if save is None:
            save_folder = get_font_install_path()
        else:
            save_folder = save
        if source == "google":
            font_list = get_google_font(font, save_folder, use_cache=use_cache)
        else:
            raise NotImplemented("Can only load from google font for now.")
        for ttf in font_list:
            fontManager.addfont(path=str(ttf.absolute()))

    if as_global:
        set_font(font)


def set_font(font):
    """

    Args:
        font: A font name

    """
    if _has_font(font):
        # explicitly ask matplotlib to recache the font
        old_params = rcParams['font.family']
        if isinstance(old_params, str):
            old_params = [old_params]
        rcParams['font.family'] = [font, *old_params]
    else:
        _raise_font_no_exist(font)


def current_font():
    return rcParams['font.family']


def list_fonts():
    return sorted(_get_current_fonts_name())


def add_ttf(ttf_font):
    fontManager.addfont(path=str(ttf_font))


def font_table(font):
    if not _has_font(font):
        _raise_font_no_exist(font)
    table = Table(title=font)
    table.add_column("Name")
    table.add_column("Style")
    table.add_column("Variant")
    table.add_column("Weight")
    table.add_column("Stretch")

    for fe in fontManager.ttflist:
        if fe.name == font:
            table.add_row(
                fe.name, fe.style, fe.variant, str(fe.weight), fe.stretch
            )
    console = Console()
    console.print(table)


def show(font):
    _, ax = plt.subplots()
    ax.axis("off")
    config = dict(fontfamily=font, va="center", ha="center")
    ax.text(0.5, 0.6, f"{font}", fontdict={"fontsize": 24, **config})
    ax.text(0.5, 0.4, f"Almost before we knew it,\nwe had left the ground",
            fontdict={"fontsize": 16, **config})
    return ax


def show_fonts():
    font_list = list_fonts()
    _, ax = plt.subplots()
    ax.axis("off")
    y = 1
    for font in font_list:
        ax.text(0.5, y, str(font),
                fontdict=dict(fontfamily=font, ha="center",
                              va="center", size=14))
        y -= 0.1
    return ax
