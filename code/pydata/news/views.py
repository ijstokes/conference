from django.shortcuts       import render_to_response

from news.models            import NewsItem
from utilities.utilities    import get_base_out_vars
from sponsors.models        import SponsorLevel
from pydata.settings        import CURRENT_CONF_ID

def view_news(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    news = NewsItem.objects.all()
    if not request.user.is_staff:
        news = news.filter(publish=True)
    output['news'] = news
    output['levels'] = SponsorLevel.objects.filter(conference__exact=CURRENT_CONF_ID)

    return render_to_response('base/templates/news/news.html', output)
