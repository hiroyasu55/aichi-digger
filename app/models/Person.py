import pandas as pd
import app.models.Datastore as Datastore
import app.lib.log as log


logger = log.getLogger(__name__)
KIND = 'Person'


def insert(person):
    entity = Datastore.insert(KIND, person)
    return Datastore.entity_to_dict(entity)


def update(person):
    entity = Datastore.update(KIND, person, 'no')
    return Datastore.entity_to_dict(entity)


def upsert(person):
    entity = Datastore.upsert(KIND, person, 'no')
    if entity:
        logger.debug('Upsert person %s', person['no'])
    else:
        logger.debug('Upsert NG person %s', person['no'])
    return Datastore.entity_to_dict(entity)


def find(filters=[], order=[], offset=0, limit=None):
    if 'no' not in order:
        order.append('no')
    entities = Datastore.find(
        KIND, filters=filters, order=order, offset=offset, limit=limit)
    persons = list(map(lambda e: Datastore.entity_to_dict(e), entities))
    return persons


def find_by_no(no):
    entity = Datastore.find_one(KIND, key='no', value=no)
    return Datastore.entity_to_dict(entity)


def delete_by_no(no):
    logger.debug('delete %s', 'no')
    entity = Datastore.delete_one(KIND, key='no', value=no)
    return Datastore.entity_to_dict(entity)


def count(filters=[]):
    return Datastore.count(KIND, filters)
