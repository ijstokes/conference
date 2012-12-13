from utilities.utilities import send_plain_email


def process_speaker_proposal(proposal):
    recipient = 'pydataconf@continuum.io'

    email_template = """
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
    confirm_email = """
    Thank you for your submission to speak at PyData Silicon Valley 2013.  We will review your
    proposal and inform you of our decision.

    If you have any questions please contact pydataconf@continuum.io.


    """
    message = email_template.format(proposal.speaker_name, proposal.title, proposal.abstract, proposal.speaker_email, proposal.bio, proposal.additional_info)
    send_plain_email(recipient, message, subject='PyData SV2013 Presentation Proposal')
    confirm_message = confirm_email + message
    send_plain_email(proposal.speaker_email, confirm_message, subject='Thank you for your PyData SV2013 Presentation Proposal')

    return message
