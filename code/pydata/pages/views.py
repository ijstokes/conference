# Create your views here.
from django.http import HttpResponse
from django.template import Context, Template, loader

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
    output['page'] = kwargs['page']
    output['conf'] = kwargs.get('conf', 'base')
    output['conf_style'] = kwargs.get('conf_style', output['conf'])

    output['page_path'] = '{0}/pages/{1}'.format(output['page'], output['conf'])

    output['title'] = '{0}'


    wrapper_path = '{0}{1}'.format(output['conf_style'], WRAPPER_TEMPLATE)

    t = loader.get_template(wrapper_path)
    outs = t.render(output)

    #'kwargs = {3}<br/>page={0}, conf={1}, conf_style={2}'.format(page, conf, conf_style, kwargs)

    return HttpResponse(outs)
