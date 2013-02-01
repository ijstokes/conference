from speakers.models import Speaker, Presentation
from django.shortcuts import render_to_response
from utilities.utilities import get_base_out_vars
from sponsors.models import SponsorLevel
# Create your views here.


def view_speakers(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    speakers = Speaker.objects.exclude(presentation__scheduleditem__itemType__name='Keynote')
    output['speakers'] = speakers.exclude(name="TBD")
    output['levels'] = SponsorLevel.objects.filter(conference__exact=1)

    return render_to_response('sv2013/templates/speaking/bios.html', output)


def view_abstracts(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    abstracts = Presentation.objects.exclude(scheduleditem__itemType__name='Keynote')
    output['abstracts'] = abstracts.exclude(title="Waiting for confirmation.")
    output['levels'] = SponsorLevel.objects.filter(conference__exact=1)

    return render_to_response('sv2013/templates/speaking/abstracts.html', output)


def view_keynotes(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    keynotes = Speaker.objects.filter(presentation__scheduleditem__itemType__name='Keynote')
    output['keynotes'] = keynotes.order_by('-name')
    output['levels'] = SponsorLevel.objects.filter(conference__exact=1)

    return render_to_response('sv2013/templates/speaking/keynotes.html', output)
