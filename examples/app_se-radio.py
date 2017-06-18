from collections import OrderedDict
from urllib.parse import urlparse

from pymongo import MongoClient

from dark_keeper import DarkKeeper

base_url = 'http://www.se-radio.net/'
domain = urlparse(base_url).netloc

menu_model = [
    '.home .entry .post-title a',  # css-selectors with menu links
    '.home .navigation a',
]

model = OrderedDict([
    ('title', '.single h1.post-title'),  # col 1
    ('desc', '.single .entry'),  # col 2
    ('mp3', '.single .powerpress_links_mp3 .powerpress_link_d'),  # col 3
])

mongo_client = MongoClient('localhost', 27017)
db_name = 'podcasts'
coll_name = domain

dk = DarkKeeper(
    base_url, menu_model, model, domain,  # create DarkKeeper
    db_name, coll_name, mongo_client
)
dk.run()  # run process
