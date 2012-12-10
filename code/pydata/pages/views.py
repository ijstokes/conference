# Create your views here.
from re import sub
from django.http import HttpResponse
from django.template import Context, loader

NOT_FOUND = r'/templates/not_found.html'
WRAPPER_TEMPLATE = '/templates/wrapper.html'

# def wrap_page(request, page, conf=None, conf_style=None):


def wrap_page(request, **kwargs):
    """
    Wrap a static page in the template (headers, css, background, etc.)
    of a conference.

    page = name of the page to be wrapped
    conf = conference directory where the page is located
    conf_style = conference wrapper file to use

    If no conf given, look in the "base" directory
    If no conf_style give, assume same as conf
    If no conf and conf_style given, both will be "base"
    If no page is found with the name return wrapped 404 page

    """

    output = Context({})
    output['page_id'] = kwargs.get('page', 'home')
    output['conf_id'] = kwargs.get('conf', 'sv2013')
    output['conf_style_id'] = kwargs.get('conf_style', output['conf_id'])
    output['navmenu'] = output['conf_style_id'] + '/templates/navmenu.html'
    output['sponsors'] = output['conf_style_id'] + '/templates/sponsors.html'
    output['head'] = output['conf_style_id'] + '/templates/header.html'
    output['header'] = output['conf_style_id'] + '/templates/head.html'
    output['banner'] = output['conf_style_id'] + '/templates/banner.html'
    output['scripts'] = output['conf_style_id'] + '/templates/scripts.html'
	

    page_name = sub(r'(.*)-(.*)', r'\1 (\2)', output['page_id'].capitalize().replace('_', ' '))
    file_name = output['page_id'] + '.html'

    output['title'] = page_name

    output['page_path'] = output['conf_id'] + '/pages/' + file_name

    return HttpResponse(loader.get_template(output['conf_style_id'] + WRAPPER_TEMPLATE).render(output))
