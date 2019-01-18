from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")
# register.filter('isMember', utils.isMember)

@register.filter(name='isMember')
def has_group(user, groupName):
    return user.groups.filter(name="pvr_admin").exists()
