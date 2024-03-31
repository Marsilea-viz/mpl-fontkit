import json
import zipfile
from pathlib import Path

import httpx
from httpx import HTTPError


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
        f"https://fonts.google.com/download/list?family={font_family}"
    filename = store_path / f"{font_family}.zip"
    if use_cache & (filename.exists()):
        return extract_font(filename, store_path)
    else:
        try:
            res = httpx.get(download_url)
            text = res.text
            index = text.find('{')
            if index != -1:
                text = text[index:]
            records = json.loads(text)['manifest']['fileRefs']
            with zipfile.ZipFile(filename, "w") as f:
                for record in records:
                    url = record['url']
                    name = Path(record['filename']).name
                    res = httpx.get(url)
                    with f.open(name, 'w') as tff:
                        tff.write(res.content)
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
                res = httpx.get(base_url + ttf_file, follow_redirects=True)
                with open(filename, 'wb') as f:
                    f.write(res.content)
            except Exception as e:
                raise ConnectionError("Network issue")
            finally:
                font_list.append(filename)

    # merged_font = store_path / "Font-Awesome.ttf"
    # ttf = Merger().merge(font_list)
    # print(ttf['name'])
    # ttf.save(merged_font)

    return font_list
