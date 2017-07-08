import os

from pymongo import MongoClient

from dark_keeper.log import Logger


def test_logger_export_mongo(cache_dir):
    mongo_client = MongoClient('localhost', 27017)
    mongo_db_name = 'podcasts_tests'
    mongo_coll_name = os.path.basename(cache_dir)

    message = 'test message for collection {}'.format(mongo_coll_name)
    log = Logger(
        mongo_client,
        mongo_db_name,
        mongo_coll_name
    )
    log.info(message)

    db = getattr(mongo_client, mongo_db_name)

    coll = getattr(db, '{}_log'.format(mongo_coll_name))
    log_message = coll.find_one()

    assert log_message['level'] == 'info'
    assert log_message['message'] == message
