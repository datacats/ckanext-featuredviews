import db
import logging
import ckan.model as model

from ckan.plugins.toolkit import get_validator, ValidationError
from ckan.lib.dictization import table_dictize
from ckan.logic import NotFound

import ckan.lib.navl.dictization_functions as df

log = logging.getLogger(__name__)

schema = {
    'resource_view_id': [get_validator('not_empty'), unicode],
    'package_id': [get_validator('ignore_empty'), unicode],
    'canonical': [get_validator('boolean_validator'), unicode],
    'homepage': [get_validator('boolean_validator'), unicode]
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
    featured.canonical = data.get('canonical', False)
    featured.homepage = data.get('homepage', False)

    resource_id = model.ResourceView.get(featured.resource_view_id).resource_id
    featured.package_id = model.Package.get(resource_id).package_id

    featured.save()

    session = context['session']
    session.add(featured)
    session.commit()

    return table_dictize(featured, context)

def featured_show(context, data_dict):
    data, errors = df.validate(data_dict, schema_get, context)

    if errors:
        raise ValidationError(errors)

    featured = db.Featured.get(resource_view_id=data['resource_view_id'])
    if featured is None:
        raise NotFound()

    return table_dictize(featured, context)

def featured_upsert(context, data_dict):
    data, errors = df.validate(data_dict, schema, context)

    if errors:
        raise ValidationError(errors)

    featured = db.Featured.get(resource_view_id=data['resource_view_id'])
    if featured is None:
        featured = db.Featured()

    featured.resource_view_id = data['resource_view_id']

    if data.has_key('canonical'):
        featured.canonical = data['canonical']

    if data.has_key('homepage'):
        featured.homepage = data['homepage']

    resource_id = model.ResourceView.get(featured.resource_view_id).resource_id
    featured.package_id = model.Resource.get(resource_id).package_id

    featured.save()

    session = context['session']
    session.add(featured)
    session.commit()

    return table_dictize(featured, context)
