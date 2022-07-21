from core.utils import get_cities, get_countries, get_urls


def test_get_countries():
    text = """Remember me
Forgot Password?
Login

Vegan & Vegetarian Restaurants in South America
 South America
South America (6682 listings)
View all areas listed alphabetically

Argentina
Bolivia
Brazil
Chile
Colombia
Ecuador
Guyana
Paraguay
Peru
Uruguay
Venezuela
Also: Trinidad and Tobago

For vegetarian organizations in South America, visit: IVU

All areas listed alphabetically
VeganVegan
VegetarianVegetarian
VegFriendlyVeg-Options
Chains
Filters0
Argentina
(959)
Bolivia
(108)
Brazil
(2913)
Chile
(754)
Colombia
(922)
Ecuador
(294)
French Guiana
(2)
Guyana
(7)
Nicaragua
(1)
Panama
(1)
Paraguay
(41)
Peru
(498)
Suriname
(6)
Uruguay
(150)
Venezuela
(26)
Share
Advertisement
"""
    countries = get_countries(text)
    assert countries == [
        "Argentina",
        "Bolivia",
        "Brazil",
        "Chile",
        "Colombia",
        "Ecuador",
        "French Guiana",
        "Guyana",
        "Nicaragua",
        "Panama",
        "Paraguay",
        "Peru",
        "Suriname",
        "Uruguay",
        "Venezuela",
    ]


def test_get_cities():
    text = """Remember me
Forgot Password?
Login

Vegan & Vegetarian Restaurants in South America
 South America
South America (6682 listings)
View all areas listed alphabetically

Argentina
Bolivia
Brazil
Chile
Colombia
Ecuador
Guyana
Paraguay
Peru
Uruguay
Venezuela
Also: Trinidad and Tobago

For vegetarian organizations in South America, visit: IVU

All areas listed alphabetically
VeganVegan
VegetarianVegetarian
VegFriendlyVeg-Options
Chains
Filters0
Argentina
(959)
Bolivia
(108)
Brazil
(2913)
Share
Advertisement
"""
    cities = get_cities(text)
    assert cities == [
        ("Argentina", "959"),
        ("Bolivia", "108"),
        ("Brazil", "2913"),
    ]


def test_get_urls():
    html = """<div id="full-site-content"><div class="region-panel-list">
            <div class="break-inside-avoid border border-gray-200 p-2 mb-1 rounded-md font-normal b7c96">
                <a href="/africa/kenya/" title="Kenya" class="block">
                    <div class="flex justify-between">
                        <div class="text-primary-500">Kenya</div>
                        <div>(94)</div>
                    </div>
                </a>
            </div>
            <div class="break-inside-avoid border border-gray-200 p-2 mb-1 rounded-md font-normal a1cb4">
                <a href="/africa/liberia/" title="Liberia" class="block">
                    <div class="flex justify-between">
                        <div class="text-primary-500">Liberia</div>
                        <div>(2)</div>
                    </div>
                </a>
            </div>
            </div>
            </div>"""
    urls = get_urls(html)
    assert urls == [["Kenya", "africa", "kenya"], ["Liberia", "africa", "liberia"]]
