import time

import pandas as pd
from utils import change_url, copy_text, get_countries, get_page_source, get_urls

CONTINENTS = [
    "https://www.happycow.net/north_america/",
    "https://www.happycow.net/europe/",
    "https://www.happycow.net/oceania/",
    "https://www.happycow.net/asia/",
    "https://www.happycow.net/south_america/",
    "https://www.happycow.net/africa/",
]

GET_STATES = [
    "https://www.happycow.net/north_america/usa",
    "https://www.happycow.net/north_america/canada/",
]

time.sleep(10)

countries = set()
urls = []
for continent in CONTINENTS:
    change_url(continent)
    countries = countries.union(set(get_countries(copy_text())))
    source = get_page_source()
    urls.extend(get_urls(source))
    time.sleep(5)

states = set()
for country in GET_STATES:
    change_url(country)
    states = states.union(set(get_countries(copy_text())))
    source = get_page_source()
    urls.extend(get_urls(source))
    time.sleep(5)


new_set = (countries.difference(set(["Canada", "USA"]))).union(states)
df = pd.DataFrame(list(new_set), columns=["name"])
urls_df = pd.DataFrame(urls, columns=["name", "continent", "country"])
df = df.merge(urls_df, how="left", on="name")
df.to_csv("countries.csv")
