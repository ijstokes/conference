from speakers.models import ProposalForm
from speakers.functions import process_speaker_proposal
from django.http import HttpResponse
from django.shortcuts import render
from utilities.utilities import get_base_out_vars
# Create your views here.


def submit_talk(request):
    output = get_base_out_vars(request)
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            new_proposal = form.save()
            message = process_speaker_proposal(new_proposal)
            return HttpResponse(message)
    else:
        form = ProposalForm()

    output['form'] = form

    return render(request, 'sv2013/templates/propose.html', output)
