from django.shortcuts import render_to_response

from speakers.models import Speaker, Presentation
from utilities.utilities import get_base_out_vars
from sponsors.models import SponsorLevel

from pydata.settings import CURRENT_CONF_ID
# Create your views here.


def view_speakers(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    conference = kwargs['conference']
    speakers = Speaker.objects.exclude(presentation__scheduleditem__itemType__name='Keynote')
    speakers = speakers.filter(presentation__conference__name=conference)
    output['speakers'] = speakers.exclude(name="TBD")
    output['levels'] = SponsorLevel.objects.filter(conference__exact=CURRENT_CONF_ID)

    return render_to_response('%s/templates/speaking/bios.html' % conference, output)


def view_abstracts(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    conference = kwargs['conference']
    abstracts = Presentation.objects.exclude(scheduleditem__itemType__name='Keynote')
    abstracts = abstracts.filter(conference__name=conference)
    output['abstracts'] = abstracts.exclude(title="Waiting for confirmation.")
    output['levels'] = SponsorLevel.objects.filter(conference__exact=CURRENT_CONF_ID)

    return render_to_response('%s/templates/speaking/abstracts.html' % conference, output)


def view_keynotes(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    conference = kwargs['conference']
    keynotes = Speaker.objects.filter(presentation__scheduleditem__itemType__name='Keynote',presentation__conference__name=conference)
    output['keynotes'] = keynotes.order_by('-name')
    output['levels'] = SponsorLevel.objects.filter(conference__exact=CURRENT_CONF_ID)

    return render_to_response('%s/templates/speaking/keynotes.html' % conference, output)
