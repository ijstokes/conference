from speakers.models import Speaker, Presentation
from django.shortcuts import render_to_response
from utilities.utilities import get_base_out_vars
# Create your views here.


def view_speakers(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    speakers = Speaker.objects.exclude(presentation__scheduleditem__itemType__name='Keynote')
    output['speakers'] = speakers.exclude(name="TBD")

    return render_to_response('sv2013/templates/speaking/bios.html', output)


def view_abstracts(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    abstracts = Presentation.objects.exclude(scheduleditem__itemType__name='Keynote')
    output['abstracts'] = abstracts.exclude(title="Waiting for confirmation.")

    return render_to_response('sv2013/templates/speaking/abstracts.html', output)
