from django import template

register = template.Library()

@register.simple_tag
def search_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystr = urlencode.split('&')
        filtered_querystr = filter(lambda p: p.split('=')[0]!=field_name, querystr)
        encoded_querystr = '&'.join(filtered_querystr)
        url = '{}&{}'.format(url, encoded_querystr)

    return url

@register.filter
def summary_data(mapping, key):
    return

