from django.core.exceptions import ObjectDoesNotExist
#from speakers.models import Proposal, ProposalForm
from speakers.functions import process_speaker_proposal
from django.shortcuts import render
from utilities.utilities import get_base_out_vars
# Create your views here.


# def submit_proposal(request, **kwargs):
#     output = get_base_out_vars(request, **kwargs)
#     if request.method == 'POST':
#         form = ProposalForm(request.POST)
#         if form.is_valid():
#             new_proposal = form.save()
#             process_speaker_proposal(new_proposal)
#             output['proposal'] = new_proposal
#             template = 'sv2013/templates/speaking/propose_view.html'
#     else:
#         proposal_id = kwargs.get('proposal', None)
#         if proposal_id:
#             proposal = Proposal.objects.get(pk=proposal_id)
#             form = ProposalForm(instance=proposal)
#         else:
#             form = ProposalForm()
#         template = 'sv2013/templates/speaking/propose.html'

#     output['form'] = form

#     return render(request, template, output)


# def view_proposal(request, **kwargs):
#     output = get_base_out_vars(request, **kwargs)
#     proposal_id = kwargs.get('id', None)
#     try:
#         output['proposal'] = Proposal.objects.get(pk=proposal_id)
#         template = 'sv2013/templates/speaking/propose_view.html'
#     except ObjectDoesNotExist:
#         output['proposals'] = Proposal.objects.all()
#         template = 'sv2013/templates/speaking/propose_all.html'

#     return render(request, template, output)


# def view_all(request):
#     output = get_base_out_vars(request)
#     output['proposals'] = Proposal.objects.all()

#     return render(request, 'sv2013/templates/speaking/propose_all.html', output)
