from re                             import sub
from datetime                        import datetime

from django.http                    import HttpResponse
from django.template                import loader, TemplateDoesNotExist
from django.views.decorators.csrf   import csrf_exempt

from pages.functions                import get_file_contents, set_file_contents
from utilities.utilities            import get_base_out_vars

from sponsors.models                import Sponsor, SponsorLevel
from events.models                  import Conference
from news.models                     import NewsItem

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


    conference      = output['conference']
    NOT_FOUND       = '%s/templates/not_found.html'         % conference
    DEFAULT_WRAPPER = '%s/templates/wrapper.html'           % conference
    HOME_WRAPPER    = '%s/templates/home_wrapper.html'      % conference
    NOSIDE_WRAPPER  = '%s/templates/noside_wrapper.html'    % conference
    EDIT_WRAPPER    = '%s/templates/edit_page.html'         % conference

    NO_SIDE = ['venue', 'sponsor/sponsors', ]

    if (kwargs.get('about',None)):
        output['page_path'] =  '%s/pages/about/' % conference + file_name
    else:
        output['page_path'] = '%s/pages/' % conference + file_name
    

    has_side = True
    ## Decide which wrapper to use
    wrapper_template = DEFAULT_WRAPPER
    if output['page_id'] == 'home':
        wrapper_template = HOME_WRAPPER
        output['all_sponsors'] = []
        levels = SponsorLevel.objects.filter(conference__name=conference)
        for level in levels:
            output['all_sponsors'].extend(level.sponsors.all())
        news = NewsItem.objects.all()
        if not request.user.is_staff:
            news = news.filter(publish=True)
        output['news'] = news.filter(date__lte=datetime.now())[:5]
        has_side = False
    if output['page_id'] in NO_SIDE:
        wrapper_template = NOSIDE_WRAPPER
        has_side = False

    if has_side:
        output['levels'] = SponsorLevel.objects.filter(conference__name=conference)

    editable = request.GET.get('edit', 0)

    if request.method == 'POST':
        editable = 0
        page_contents = request.POST['page_contents']
        set_file_contents(output['page_path'], page_contents)

    if editable == '1' and request.user.is_staff:
        output['page_contents'] = get_file_contents(output['page_path'])
        output['repost_link'] = request.path_info
        template = loader.get_template(EDIT_WRAPPER).render(output)
    else:
        #try:
        template = loader.get_template(wrapper_template).render(output)
        #except TemplateDoesNotExist:
        #    template = loader.get_template(NOT_FOUND).render(output)

    response = HttpResponse(template)

    return response

@csrf_exempt
def common(request, **kwargs):
    """
    PyData Common Content
    """

    site                = 'base'
    NO_SIDE             = ['sponsors', ]

    output = get_base_out_vars(request, conference=site, **kwargs)

    output['page_id']   = kwargs.get('page', 'home')
    file_name           = output['page_id'] + '.html'
    output['title']     = sub(r'(.*)-(.*)', r'\1 (\2)', output['page_id'].capitalize().replace('_', ' '))
    output['page_path'] = '%s/pages/' % site + file_name

    NOT_FOUND           = '%s/templates/not_found.html'         % site
    DEFAULT_WRAPPER     = '%s/templates/wrapper.html'           % site
    HOME_WRAPPER        = '%s/templates/home_wrapper.html'      % site
    NOSIDE_WRAPPER      = '%s/templates/noside_wrapper.html'    % site
    EDIT_WRAPPER        = '%s/templates/edit_page.html'         % site

    
    has_side = True
    ## Decide which wrapper to use
    wrapper_template = DEFAULT_WRAPPER
    if output['page_id'] == 'home':
        wrapper_template = HOME_WRAPPER
        output['all_sponsors'] = []
        levels = SponsorLevel.objects.filter(conference__name=site)
        for level in levels:
            output['all_sponsors'].extend(level.sponsors.all())
        news = NewsItem.objects.all()
        if not request.user.is_staff:
            news = news.filter(publish=True)
        output['news'] = news.filter(date__lte=datetime.now())[:5]
        has_side = False

    if output['page_id'] in NO_SIDE:
        wrapper_template = NOSIDE_WRAPPER
        has_side = False

    if has_side:
        pass # nothing to do now

    editable = request.GET.get('edit', 0)

    if request.method == 'POST':
        editable = 0
        page_contents = request.POST['page_contents']
        set_file_contents(output['page_path'], page_contents)

    if editable == '1' and request.user.is_staff:
        output['page_contents'] = get_file_contents(output['page_path'])
        output['repost_link'] = request.path_info
        template = loader.get_template(EDIT_WRAPPER).render(output)
    else:
        template = loader.get_template(wrapper_template).render(output)

    response = HttpResponse(template)

    return response
