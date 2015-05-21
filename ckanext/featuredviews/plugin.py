import actions
import ckan.model as model
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.dictization.model_dictize as md

from db import Featured

class FeaturedviewsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'featured')

    def get_actions(self):
        actions_dict = {
            'featured_create': actions.featured_create,
            'featured_show': actions.featured_show,
            'featured_update': actions.featured_update
        }
        return actions_dict

    def get_helpers(self):
        helpers = {
            'get_canonical_resource_view': _get_canonical_view,
            'get_homepage_resource_views': _get_homepage_views
        }
        return helpers

def _get_canonical_view(package_id):
    canonical = Featured.find(package_id=package_id, canonical=True).first()

    resource_view = md.resource_view_dictize(
        model.ResourceView.get(canonical.resource_view_id), {'model': model}
    )
    resource = md.resource_dictize(
        model.Resource.get(resource_view['resource_id']), {'model': model}
    )

    return {'resource': resource, 'resource_view': resource_view}

def _get_homepage_views():
    homepage = Featured.find(homepage=True).all()

    return homepage
