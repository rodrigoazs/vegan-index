import time

import pandas as pd
from utils import change_url, copy_text, get_countries, get_page_source, get_urls

FILTERS = [
    "?filters=vegan",
    "?filters=vegetarian",
    "?filters=vegfriendly-chains",
    "?filters=bakery-bnb-catering-coffee-delivery-farmers-foodtruck-health-icecream-juicebar-marketvendor-organization-other-veganprofessional-spa-vegshop",
]

df = pd.read_csv("countries.csv")

time.sleep(10)
