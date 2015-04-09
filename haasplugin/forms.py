from django import forms

class ProjectForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Project name')
    action = '/projects/create'
    back_link = '/projects'
    back_text = 'Cancel'
    submit = 'Create'


class DeleteProjectForm(forms.Form):
    """description of class"""
    name = forms.CharField(label='Delete Project')
    action = '/projects/delete'
    back_text = 'Cancel'
    submit = 'Delete'

class AllocateNodeForm(forms.Form):
    node_name = forms.CharField(widget=forms.HiddenInput())
    action = "/projects/details/connect_node"

class DetachNodeForm(forms.Form):
    node_name = forms.CharField(widget=forms.HiddenInput())
    submit = "Detach"

class HeadnodeForm(forms.Form):
    name = forms.CharField(label='Headnode Name')
    base_img = forms.CharField(label='Base Image')
    project = forms.CharField(label='Project')
    action = '/headnode/create/'
    back_link = '/projects/details/'
    back_text = 'Cancel'
    submit = 'Create'


