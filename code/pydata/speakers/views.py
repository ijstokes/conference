from speakers.models import ProposalForm
from django.http import HttpResponse
from django.shortcuts import render
from utilities.utilities import send_plain_email, get_out_vars
# Create your views here.


def submit_talk(request):
    output = get_out_vars(request)
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            recipient = 'trentoliphant@gmail.com'
            title = form.cleaned_data['title']
            abstract = form.cleaned_data['abstract']
            bio = form.cleaned_data['bio']
            additional = form.cleaned_data['additional']
            name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']

            template = """
            Proposal from {0} ({3}):
            ===================================================
            Title:
            {1}

            Abstract:
            {2}

            Presenter: {0}
            Email: {3}
            Bio: {4}

            Additonal Info:
            {5}
            """
            message = template.format(name, title, abstract, email, bio, additional)
            send_plain_email(recipient, message, subject='PyData SV2103 Presentation Proposal')

            return HttpResponse(message)
    else:
        form = ProposalForm()

    output['form'] = form

    return render(request, 'sv2013/templates/propose.html', output)

