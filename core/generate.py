import re

import pandas as pd
from bs4 import BeautifulSoup

columns_files = {
    "check": "brazil_all.html",
    "vegan": "brazil_vegan.html",
    "vegetarian": "brazil_vegetarian.html",
    "veg_options": "brazil_veg_options.html",
    "others": "brazil_others.html",
}

final_df = None
for column, f in columns_files.items():
    f = open(f, "r")
    page_content = f.read()

    soup = BeautifulSoup(page_content, "html.parser")

    results = soup.find(id="full-site-content")

    job_elements = results.find_all("div", class_="break-inside-avoid")

    data = []
    for job_element in job_elements:
        nes = job_element.find_all("div")
        match = re.search(r"\(([0-9]+)\)", nes[2].next)
        city = nes[1].next
        amount = match.groups()[0]
        data.append([city, amount])

    df = pd.DataFrame(data, columns=["city", column])
    if final_df is not None:
        final_df = final_df.merge(df, how="left", on="city")
    else:
        final_df = df

final_df = final_df.fillna(0)
for key in columns_files.keys():
    final_df[key] = final_df[key].astype("int")
final_df["total"] = (
    final_df["vegan"]
    + final_df["vegetarian"]
    + final_df["veg_options"]
    + final_df["others"]
)

to_remove = final_df[final_df["total"] != final_df["check"]]
print(to_remove)
print(to_remove["city"].tolist())

fake = [
    "Njnindex",
    "Ztundbim",
    "Ytfmzdmz",
    "Nzaodymt",
    "Nmyowynd",
    "Mrkntnlm",
    "Ndzhnzbk",
    "Mmynjmmz",
    "Otgzytio",
    "Mgunjawn",
]

final_df = final_df[~(final_df["city"].isin(fake))]
final_df = final_df.drop(columns=["check"])
final_df.to_csv("brazil.csv")
