"""
Definition of urls for haasplugin.
"""

from django.conf.urls import patterns, include, url
from haasplugin.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'haasplugin.views.home', name='home'),
    # url(r'^haasplugin/', include('haasplugin.haasplugin.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'(?:.*?/)?(?P<path>(images)/.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
    url(r'^projects/(?P<name>.+)/attach_node', allocate_node),  
    url(r'^projects/(?P<name>.+)/assign_headnode', allocate_node),  
    url(r'^projects/(?P<name>.+)/detach_node', detach_node),
    url(r'^projects/(?P<name>.+)/detach_headnode', detach_node), 
    url(r'^projects/(?P<name>.+)/hnic_add', hnic_add),
    url(r'^project_create', project_create),
    url(r'^project_delete', project_delete),
    url(r'^projects/(?P<project>.+)/headnodes/(?P<name>.+)/headnode_delete', headnode_delete),
    url(r'^projects/(?P<project>.+)/headnodes/(?P<name>.+)/start', headnode_start),
    url(r'^projects/(?P<project>.+)/headnodes/(?P<name>.+)/stop', headnode_stop),
    url(r'^headnode_delete', headnode_delete),
    url(r'^headnode_create', headnode_create),
    url(r'^headnodes/(?P<name>.+)/headnode_delete_hnic/(?P<hnic>.+)', headnode_delete_hnic),
    url(r'^headnodes/(?P<name>.+)/hnic_add', hnic_add), 
    url(r'^headnodes/(?P<name>.+)', headnode_details), 
    url(r'^node_create', node_create),
    url(r'^node_delete', node_delete),
    url(r'^network_create', network_create), 
    url(r'^network_delete', network_delete), 
    url(r'^network_project_create', network_project_create),
    url(r'^projects/(?P<name>.+)', project_details),
    url(r'^nodes/(?P<name>.+)/node_register_nic', node_register_nic),
    url(r'^nodes/(?P<name>.+)/node_delete_nic/(?P<nic>.+)', node_delete_nic),
    url(r'^nodes/(?P<name>.+)/power_cycle', node_powercycle),
    url(r'^nodes/(?P<name>.+)', node_details), 
    #url(r'^networks/(?P<name>.+)', network_details), #change project_details to network_details here and create it in views.py
    url(r'^projects/', projects),
    url(r'^nodes/', nodes),
    url(r'^networks/', networks),
    
    url(r'^$', projects),
  
)
