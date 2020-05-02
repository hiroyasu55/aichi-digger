from google.cloud import datastore
from datetime import datetime
import app.lib.log as log


logger = log.getLogger(__name__)
client = datastore.Client()


def now_string():
    return datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')


def entity_to_dict(data):
    if data is None:
        return data

    if data.__class__.__name__ == 'Entity':
        data = dict(data)

    if type(data) is dict:
        for key in data:
            data[key] = entity_to_dict(data[key])
    elif type(data) is list:
        data = list(map(lambda d: entity_to_dict(d), data))

    return data


def insert(kind, object):
    entity_key = client.key(kind)
    entity = datastore.Entity(entity_key)
    entity.update(object)
    entity.update({'created': now_string(), 'updated': now_string()})
    client.put(entity)
    logger.debug('insert')
    entity['id'] = entity.key.id

    return entity


def update(kind, object, key):
    entity = find_one(kind, key=key, value=object.get(key))
    if not entity:
        raise Exception('Entity not found. kind={},:key={},value={}', kind, key, key.get(key))

    entity.update(object)
    entity.update({'updated': now_string()})
    client.put(entity)
    logger.debug('update')
    entity['id'] = entity.key.id

    return entity


def upsert(kind, object, key=None):
    entity = None
    if key:
        entity = find_one(kind, key=key, value=object.get(key))
        if entity:
            entity.update(object)
            entity.update({'updated': now_string()})
            client.put(entity)
            logger.debug('upsert:update')
            entity['id'] = entity.key.id
        else:
            entity = insert(kind, object)
            logger.debug('upsert:insert')

    else:
        entity = insert(kind, object)
        logger.debug('upsert:insert')

    return entity


def find(kind, filters=[], order=[], offset=0, limit=None):
    query = client.query(kind=kind)
    for f in filters:
        symbol = f.get('symbol') or '='
        query.add_filter(f['key'], symbol, f['value'])

    query.order = order
    param = {
        'offset': offset,
        'limit': limit
    }

    entities = list(query.fetch(**param))
    return entities


def find_one(kind, key=None, value=None):
    if not key:
        raise Exception('find_one: key not defined.')
    if not value:
        raise Exception('find_one: value not defined.')

    query = client.query(kind=kind)
    query.add_filter(key, '=', value)
    entities = list(query.fetch())
    if len(entities) == 0:
        return None

    return entities[0]


def find_all(kind, order=None):
    query = client.query(kind=kind)
    if order:
        query.order = order
    entities = list(query.fetch())
    return entities


def delete_one(kind, key=None, value=None):
    if not key:
        raise Exception('delete_one: key not defined.')
    if not value:
        raise Exception('delete_one: value not defined.')

    entity = find_one(kind, key=key, value=value)
    if not entity:
        logger.warning('delete_one: entity not found.')
        return None

    client.delete(client.key(kind, entity.key.id))
    return entity


def count(kind, filters=[]):
    query = client.query(kind=kind)
    query.keys_only()
    entities = list(query.fetch())

    return len(entities)
