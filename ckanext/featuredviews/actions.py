import db
import logging

from ckan.plugins.toolkit import get_validator, ValidationError
from ckan.lib.dictization import table_dictize
from ckan.logic import NotFound

import ckan.lib.navl.dictization_functions as df

log = logging.getLogger(__name__)

schema = {
    'resource_view_id': [get_validator('not_empty'), unicode],
    'package_id': [get_validator('ignore_empty'), unicode],
    'canonical': [get_validator('ignore_empty'), unicode],
    'homepage': [get_validator('ignore_empty'), unicode]
}

schema_get = {
    'resource_view_id': [get_validator('not_empty'), unicode]
}

def featured_create(context, data_dict):
    data, errors = df.validate(data_dict, schema, context)

    if errors:
        raise ValidationError(errors)

    featured = db.Featured()
    featured.resource_view_id = data['resource_view_id']
    featured.canonical = data['canonical']
    featured.homepage = data['homepage']
    featured.save()

    session = context['session']
    session.add(featured)
    session.commit()

    return featured.resource_view_id

def featured_show(context, data_dict):
    data, errors = df.validate(data_dict, schema_get, context)

    if errors:
        raise ValidationError(errors)

    featured = db.Featured.get(resource_view_id=data['resource_view_id'])
    if featured is None:
        raise NotFound()

    return table_dictize(featured, context)

def featured_update(context, data_dict):
    data, errors = df.validate(data_dict, schema, context)

    if errors:
        raise ValidationError(errors)

    featured = db.Featured.get(resource_view_id=data['resource_view_id'])
    if featured is None:
        raise NotFound()

    featured.canonical = data['canonical']
    featured.homepage = data['homepage']
    featured.save()

    session = context['session']
    session.add(featured)
    session.commit()
