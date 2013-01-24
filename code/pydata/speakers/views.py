from speakers.models import Speaker, Presentation
from django.shortcuts import render_to_response
from utilities.utilities import get_base_out_vars
# Create your views here.


def view_speakers(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    output['speakers'] = Speaker.objects.all()

    return render_to_response('sv2013/templates/speaking/bios.html', output)


def view_abstracts(request, **kwargs):
    output = get_base_out_vars(request, **kwargs)
    output['abstracts'] = Presentation.objects.all()

    return render_to_response('sv2013/templates/speaking/abstracts', output)
