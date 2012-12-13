# Create your views here.
from re import sub
from django.http import HttpResponse
from django.template import loader, TemplateDoesNotExist
from utilities.utilities import get_base_out_vars

NOT_FOUND = r'/templates/not_found.html'

DEFAULT_WRAPPER = '/templates/wrapper.html'
HOME_WRAPPER = '/templates/home_wrapper.html'
NOSIDE_WRAPPER = '/templates/noside_wrapper.html'

NO_SIDE = ['venue', 'sponsor/sponsors' ]


def wrap_page(request, **kwargs):
    """
    Wrap a static page in the template (headers, css, background, etc.)
    of a conference.

    """

    output = get_base_out_vars(request, **kwargs)

    output['page_id'] = kwargs.get('page', 'home')
    page_name = sub(r'(.*)-(.*)', r'\1 (\2)', output['page_id'].capitalize().replace('_', ' '))
    file_name = output['page_id'] + '.html'

    output['title'] = page_name

    output['page_path'] = output['conf_id'] + '/pages/' + file_name

    ## Decide which wrapper to use
    wrapper_template = DEFAULT_WRAPPER
    if output['page_id'] == 'home':
        wrapper_template = HOME_WRAPPER
    if output['page_id'] in NO_SIDE:
        wrapper_template = NOSIDE_WRAPPER

    try:
        template = loader.get_template(output['conf_style_id'] + wrapper_template).render(output)
    except TemplateDoesNotExist:
        output['page_path'] = output['conf_id'] + NOT_FOUND
        template = loader.get_template(output['conf_style_id'] + NOT_FOUND).render(output)

    response = HttpResponse(template)

    return response
