from os import popen

from django.template import RequestContext

from pydata.settings                import CURRENT_CONF_ID, CURRENT_CONF_NAME

MAIL = '/usr/sbin/sendmail'


def send_plain_email(recipient, message, sender='admin@pydata.org', subject='Automated Email from PyData.org'):
    template = """To: {0}
From: {1}
Subject: {2}

{3}

"""
    send_string = template.format(recipient, sender, subject, message)

    p = popen(MAIL + ' -t', 'w')
    p.write(send_string)
    exitcode = p.close()

    return exitcode


def get_base_out_vars(request, **kwargs):

    output = RequestContext(request, {})
    conference              = kwargs.get('conference')
    if conference:
        conference = conference.strip()
    else:
        conference = CURRENT_CONF_NAME

    output['conference']    = conference
    output['conf_id'] = conference
    output['conf_style_id'] = conference
    output['navmenu']       = '%s/templates/navmenu.html' % conference
    output['sponsors']      = '%s/templates/sponsors.html' % conference
    output['head']          = '%s/templates/head.html' % conference
    output['header']        = '%s/templates/header.html' % conference
    output['smlheader']     = '%s/templates/smlheader.html' % conference
    output['banner']        = '%s/templates/banner.html' % conference
    output['scripts']       = '%s/templates/scripts.html' % conference
    output['sponsors']      = '%s/templates/sponsors.html' % conference
    output['footer']        = '%s/templates/footer.html' % conference
    output['sidebar']       = '%s/templates/sidebar.html' % conference

    return output
