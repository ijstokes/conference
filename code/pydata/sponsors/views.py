from sponsors.models import SponsorLevel
from django.shortcuts import render_to_response
from utilities.utilities import get_base_out_vars

# Create your views here.


def show_all_sponsors(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    levels = SponsorLevel.objects.filter(conference__exact=1)
    output['levels'] = levels
    return render_to_response('sv2013/templates/sponsors/sponsor_list.html', output)


def sponsor_info(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    levels = SponsorLevel.objects.filter(conference__exact=1)
    output['levels'] = levels
    return render_to_response('sv2013/templates/sponsors/sponsor_info.html', output)
