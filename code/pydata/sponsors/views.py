from django.shortcuts import render_to_response

from sponsors.models import SponsorLevel
from utilities.utilities import get_base_out_vars
from pydata.settings import CURRENT_CONF_ID

def show_all_sponsors(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    conference = kwargs['conference']
    levels = SponsorLevel.objects.filter(conference__exact=CURRENT_CONF_ID,conference__name=conference)
    output['levels'] = levels
    return render_to_response('%s/templates/sponsors/sponsor_list.html' % conference, output)


def sponsor_info(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    conference = kwargs['conference']
    levels = SponsorLevel.objects.filter(conference__exact=CURRENT_CONF_ID,conference__name=conference)
    output['levels'] = levels
    return render_to_response('%s/templates/sponsors/sponsor_info.html' % conference, output)
