import re

from src import READMANGA_URL


def chapters_into_dict(chapters: list) -> dict:
    regex = "[\n]+|[ ]{2,}"
    chapters = [re.sub(regex, "", chapter) for chapter in chapters]
    links = filter(lambda m: m.startswith("/"), chapters)
    names = filter(lambda n: not n.startswith("/"), chapters)

    chapters_catalogue = {}
    for link, name in zip(links, names):
        chapters_catalogue.update({READMANGA_URL + link: name})

    return chapters_catalogue


def parse_rating(rate_str: str):
    """
    >>> parse_rating("9.439212799072266 из 10")
    9.43
    """
    try:
        return float(re.match(r"^(\d\.\d{2})\d* из 10$", rate_str).group(1))
    except (AttributeError, ValueError):
        return 0.0
