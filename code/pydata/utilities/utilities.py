from os import popen
from django.template import RequestContext

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
    output['conf_id'] = kwargs.get('conference','sv2013')
    output['conf_style_id'] = kwargs.get('conference', 'sv2013')    
    output['navmenu'] = output['conf_style_id'] + '/templates/navmenu.html'
    output['sponsors'] = 'base/templates/sponsors.html'
    output['head'] = 'base/templates/head.html'
    output['header'] = 'base/templates/header.html'
    output['smlheader'] = 'base/templates/smlheader.html'
    output['banner'] = 'base/templates/banner.html'
    output['scripts'] = 'base/templates/scripts.html'
    output['sponsors'] = 'base/templates/sponsors.html'
    output['footer'] = 'base/templates/footer.html'
    output['sidebar'] = 'base/templates/sidebar.html'

    return output
