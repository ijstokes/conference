from django.shortcuts       import render_to_response

from news.models            import NewsItem
from utilities.utilities    import get_base_out_vars
from sponsors.models        import SponsorLevel
from pydata.settings        import CURRENT_CONF_ID

def view_news(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    conference = kwargs.get('conference')
    news = NewsItem.objects.filter(conference__name=conference).order_by('-date')
    if not request.user.is_staff:
        news = news.filter(publish=True)

    output['news'] = news
    output['levels'] = SponsorLevel.objects.filter(conference__name=conference)

    return render_to_response('%s/templates/news/news.html' % conference, output)
