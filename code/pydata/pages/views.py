# Create your views here.
from django.http import HttpResponse

NOT_FOUND = r'/templates/not_found.html'


# def wrap_page(request, page, conf=None, conf_style=None):

def wrap_page(request, **kwargs):
    page = kwargs['page']

    """
    Wrap a static page in the template (headers, css, background, etc.)
    of a conference.

    page = namge of the page to be wrapped
    conf = conference directory where the page is located
    conf_style = conference wrapper file to use

    If no conf given, look in the "base" directory
    If no conf_style give, assume same as conf
    If no conf and conf_style given, both will be "base"
    If no page is found with the name return wrapped 404 page

    """
    if 'conf' not in kwargs.keys():
        conf = 'base'
    else:
        conf = kwargs['conf']
    if 'conf_style' not in kwargs.keys():
        conf_style = conf
    else:
        conf_style = kwargs['conf_style']

    page_path = 'kwargs = {3}<br/>page={0}, conf={1}, conf_style={2}'.format(page, conf, conf_style, kwargs)
    return HttpResponse(page_path)
