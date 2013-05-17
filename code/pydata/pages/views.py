# Create your views here.
from pages.functions import get_file_contents, set_file_contents
from re import sub
from django.http import HttpResponse
from django.template import loader, TemplateDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from utilities.utilities import get_base_out_vars

NOT_FOUND = r'/templates/not_found.html'

DEFAULT_WRAPPER = '/templates/wrapper.html'
HOME_WRAPPER = '/templates/home_wrapper.html'
NOSIDE_WRAPPER = '/templates/noside_wrapper.html'
EDIT_WRAPPER = '/templates/edit_page.html'

NO_SIDE = ['venue', 'sponsor/sponsors', ]


@csrf_exempt
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


    conference = output['conf_id']

    template_base = 'base'

    if (kwargs.get('about',None)):
        output['page_path'] =  'pages/about/' + file_name
    else:
        output['page_path'] = 'pages/' + file_name
    

    has_side = True
    ## Decide which wrapper to use
    wrapper_template = DEFAULT_WRAPPER
    if output['page_id'] == 'home':
        wrapper_template = HOME_WRAPPER
        from sponsors.models import Sponsor
        from news.models import NewsItem
        from datetime import datetime
        output['all_sponsors'] = Sponsor.objects.filter(level__conference=1,level__conference__name=conference)
        news = NewsItem.objects.all()
        if not request.user.is_staff:
            news = news.filter(publish=True)
        output['news'] = news.filter(date__lte=datetime.now())[:5]
        has_side = False
    if output['page_id'] in NO_SIDE:
        wrapper_template = NOSIDE_WRAPPER
        has_side = False

    if has_side:
        from sponsors.models import SponsorLevel
        output['levels'] = SponsorLevel.objects.filter(conference__exact=1,conference__name=conference)

    editable = request.GET.get('edit', 0)

    if request.method == 'POST':
        editable = 0
        page_contents = request.POST['page_contents']
        set_file_contents(output['page_path'], page_contents)

    if editable == '1' and request.user.is_staff:
        output['page_contents'] = get_file_contents(output['page_path'])
        output['repost_link'] = request.path_info
        template = loader.get_template(template_base + EDIT_WRAPPER).render(output)
    else:
        try:
            template = loader.get_template(template_base + wrapper_template).render(output)
        except TemplateDoesNotExist:
            template = loader.get_template('base' + NOT_FOUND).render(output)

    response = HttpResponse(template)

    return response
