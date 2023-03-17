import zipfile
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlretrieve


def extract_font(filename, store_path):
    font_list = []
    with zipfile.ZipFile(filename, 'r') as f:
        for ttf in f.namelist():
            if Path(ttf).suffix.lower() == ".ttf":
                font_list.append(store_path / ttf)
        f.extractall(store_path)
    return font_list


def get_google_font(font_family, store_path, use_cache=True):
    store_path = Path(store_path)
    download_url = \
        f"https://fonts.google.com/download?family={quote(font_family)}"
    filename = store_path / f"{font_family}.zip"
    if use_cache & (filename.exists()):
        return extract_font(filename, store_path)
    else:
        try:
            _ = urlretrieve(download_url, filename=filename)
        except Exception as e:
            if e == HTTPError:
                raise NameError(f"{font_family} does not exist in google font")
            else:
                raise ConnectionError("Network issue")
        finally:
            return extract_font(filename, store_path)


def get_fontawesome(store_path, use_cache=True):
    base_url = "https://github.com/FortAwesome/Font-Awesome/raw/6.x/webfonts/"
    brands = "fa-brands-400.ttf"
    regular = "fa-regular-400.ttf"
    solid = "fa-solid-900.ttf"

    font_list = []
    for ttf_file in [brands, regular, solid]:
        filename = store_path / ttf_file
        if use_cache & filename.exists():
            font_list.append(filename)
        else:
            try:
                _ = urlretrieve(base_url + ttf_file, filename=filename)
            except Exception as e:
                raise ConnectionError("Network issue")
            finally:
                font_list.append(filename)

    # merged_font = store_path / "Font-Awesome.ttf"
    # ttf = Merger().merge(font_list)
    # print(ttf['name'])
    # ttf.save(merged_font)

    return font_list
