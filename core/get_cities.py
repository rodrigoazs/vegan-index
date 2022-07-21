import os
import time

import pandas as pd
from utils import change_url, copy_text, get_cities, get_page_source, get_urls

FILTERS = [
    "?filters=vegan",
    "?filters=vegetarian",
    "?filters=vegfriendly-chains",
    "?filters=bakery-bnb-catering-coffee-delivery-farmers-foodtruck-health-icecream-juicebar-marketvendor-organization-other-veganprofessional-spa-vegshop",
]

countries_df = pd.read_csv("countries.csv")

if not os.path.exists("data.csv"):
    df = pd.DataFrame(
        [],
        columns=[
            "date",
            "name",
            "continent",
            "country",
            "city",
            "vegan",
            "vegetarian",
            "vegfriendly",
            "others",
        ],
    )
    df.to_csv("data.csv")
else:
    df = pd.read_csv("data.csv")


time.sleep(10)

URL = "https://www.happycow.net/{}/{}/{}"
for i in range(5):
    for _filter in FILTERS:
        row = countries_df.iloc[i]
        name = row.name
        continent = row.continent
        country = row.country
        change_url(URL.format(continent, country, _filter))
        text = copy_text()
        if (
            "Our systems have detected unusual traffic from your computer network"
            not in text
        ):
            raise Exception(text)
        matches = get_cities(text)
        print(matches)
