from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from ..schema.bookmark import BookmarkBase


def get_meta(url: str) -> BookmarkBase:
    req = Request(url=url, headers={"User-Agent": "LinkManager/1.0"})
    with urlopen(req) as resp:
        raw_html = resp.read().decode("utf-8")
    html_doc = BeautifulSoup(raw_html, "html.parser")
    metas = html_doc.select("meta[property]")

    if not metas:
        return BookmarkBase(url=url)

    url_metadata = {
        meta.attrs["property"].split(":")[1]: meta.attrs["content"]
        for meta in metas
        if meta["property"] in ["og:title", "og:description", "og:url"]
    }

    return BookmarkBase(**url_metadata)
