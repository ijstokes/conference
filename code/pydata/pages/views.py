# Create your views here.
from re import sub
from django.http import HttpResponse
from django.template import loader, TemplateDoesNotExist
from utilities.utilities import get_base_out_vars

NOT_FOUND = r'/templates/not_found.html'
WRAPPER_TEMPLATE = '/templates/wrapper.html'
ALT_WRAPPER = '/templates/alt_wrapper.html'

# def wrap_page(request, page, conf=None, conf_style=None):


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

    try:
        template = loader.get_template(output['conf_style_id'] + WRAPPER_TEMPLATE).render(output)
    except TemplateDoesNotExist:
        output['page_path'] = output['conf_id'] + NOT_FOUND
        template = loader.get_template(output['conf_style_id'] + NOT_FOUND).render(output)

    response = HttpResponse(template)

    return response
