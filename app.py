import os
from collections import OrderedDict

from pymongo import MongoClient

from dark_keeper import DarkKeeper
from dark_keeper.menu import Menu
from dark_keeper.storage import Storage

cache_dir = os.path.join(
    os.getcwd(), 'cache', 'it-podcast.com'  # path to export directory
)
menu = Menu(
    'https://it-podcast.com/',  # base url
    [
        '.list-page .entry .title a',  # css-selectors with menu links
        '.list-page .navigation a',
    ],
)

mongo_client = MongoClient('localhost', 27017)
db_name = 'podcasts'
coll_name = os.path.basename(cache_dir)
storage = Storage(
    OrderedDict([
        ('title', '.item-page .podcast h1.title'),  # col 1
        ('desc', '.item-page .podcast .decription'),  # col 2
        ('mp3', '.item-page .podcast .mp3 a'),  # col 3
    ]),
    db_name,
    coll_name,
    mongo_client,
)

dk = DarkKeeper(
    menu, storage, cache_dir,  # create DarkKeeper
    db_name, coll_name, mongo_client
)
dk.run()  # run process
