import os

from dark_keeper import DarkKeeper
from dark_keeper.log import get_log
from dark_keeper.menu import Menu
from dark_keeper.request import Request
from dark_keeper.storage import Storage

export_dir = os.path.join(
    os.getcwd(), 'export', 'radio-t.com__one'  # path to export directory
)
menu = Menu(
    'https://radio-t.com/archives/',  # base url
    [
        '#blog-archives h1 a',  # css-selectors with menu links
    ],
)
storage = Storage(
    [
        ('title', '.hentry .entry-title'),  # col 1
        ('desc', '.hentry .entry-content'),  # col 2
        ('mp3', '.hentry audio'),  # col 3
    ],
    export_dir,
    1,  # mul for max length of strings in Excel (32767 * 1), if > 1 raise error when open in Excel)
)
request = Request(
    [1, 2],  # delay
    export_dir,
    'Mozilla/5.0 (Windows NT 10.0; WOW64) '  # user-agent
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
)
log = get_log(
    '%(asctime)s %(message)s',  # log format
    os.path.join(export_dir, 'export.log'),  # log file
)

dk = DarkKeeper(
    menu, storage, request, log  # create DarkKeeper
)
dk.run()  # run process
