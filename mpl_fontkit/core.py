from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import fontManager
from thefuzz import process
from thefuzz import fuzz

from mpl_fontkit.download import get_google_font


# try:
#     _HOME = Path.home()
# except Exception:  # Exceptions thrown by home() are not specified...
#     _HOME = Path(os.devnull)  # Just an arbitrary path with no children.
#
# MSFontInstallDir = [
#     str(_HOME / 'AppData/Local/mpl_fontkit/fonts'),
# ] + [win32FontDirectory()]
#
# f = Path(str(_HOME / 'AppData/Local/mpl_fontkit/fonts'))
# f.mkdir(exist_ok=True, parents=True)
#
# OSXFontInstallDir = [
#     str(_HOME / "Library/Fonts"),
# ]
#
# X11FontInstallDir = [
#     str((Path(os.environ.get('XDG_DATA_HOME') or _HOME / ".local/share"))
#         / "fonts"),
#     str(_HOME / ".fonts"),
# ]

def _get_current_fonts_name():
    return set([font.name for font in fontManager.ttflist])


def _get_similar_font(font):
    result, _ = process.extractOne(font, _get_current_fonts_name(), scorer=fuzz.token_sort_ratio)
    return result


def _raise_font_no_exist(font):
    similar = _get_similar_font(font)
    error_msg = f"Cannot find {font}, do you mean: {similar}. " \
                f"Use `.fonts()` to list all the available fonts."
    raise LookupError(error_msg)


def _has_font(font):
    if font in _get_current_fonts_name():
        return True
    else:
        return False


class FontKit:

    def __init__(self):
        pass

    @staticmethod
    def fonts():
        return sorted(_get_current_fonts_name())

    def get(self, font, as_global=True, save=None, source="google", use_cache=True):
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
                save_folder = self.get_font_install_path()
            else:
                save_folder = save
            if source == "google":
                font_list = get_google_font(font, save_folder, use_cache=use_cache)
            else:
                raise NotImplemented("Can only load from google font for now.")
            for ttf in font_list:
                fontManager.addfont(path=str(ttf.absolute()))

        if as_global:
            self.set_global(font)

    @staticmethod
    def add_ttf(ttf_font):
        fontManager.addfont(path=str(ttf_font))

    @staticmethod
    def set_global(font):
        """

        Args:
            font: A font name

        Returns:

        """
        if _has_font(font):
            # explicitly ask matplotlib to recache the font
            old_params = rcParams['font.family']
            if isinstance(old_params, str):
                old_params = [old_params]
            rcParams['font.family'] = [font, *old_params]
        else:
            _raise_font_no_exist(font)

    @staticmethod
    def get_font_install_path():
        # if sys.platform == 'win32':
        #     candidates = MSFontInstallDir
        # elif sys.platform == 'darwin':
        #     candidates = [*OSXFontInstallDir, *X11FontInstallDir]
        # else:
        #     candidates = X11FontInstallDir
        # install_path = None
        # for p in candidates:
        #     if Path(p).exists():
        #         install_path = p
        #         break
        # if install_path is None:
        #     # fallback to current working directory
        #     install_path = Path()
        install_path = Path(".fonts")
        install_path.mkdir(exist_ok=True)
        return install_path

    @staticmethod
    def show(font):
        _, ax = plt.subplots()
        ax.axis("off")
        config = dict(fontfamily=font, va="center", ha="center")
        ax.text(0.5, 0.6, f"{font}", fontdict={"fontsize": 24, **config})
        ax.text(0.5, 0.4, f"Almost before we knew it,\nwe had left the ground",
                fontdict={"fontsize": 16, **config})
        return ax

    @staticmethod
    def font_table(font):
        avails = [
            ["Name", "Style", "Variant", "Weight", "Stretch"],
            ["----", "-----", "-------", "-----", "-------"],
        ]
        for fe in fontManager.ttflist:
            if fe.name == font:
                avails.append([
                    fe.name, fe.style, fe.variant, fe.weight, fe.stretch
                ])
        if len(avails) == 2:
            _raise_font_no_exist(font)
        else:
            for row in avails:
                print('{:^8}  {:^8}  {:^8}  {:^8}  {:^8}'.format(*row))

    def show_fonts(self):
        font_list = self.fonts()
        _, ax = plt.subplots()
        ax.axis("off")
        y = 1
        for font in font_list:
            ax.text(0.5, y, str(font), fontdict=dict(fontfamily=font, ha="center", va="center", size=14))
            y -= 0.1
        return ax
