from os import popen
from django.template import Context

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

    output = Context({})
    output['conf_id'] = kwargs.get('conf', 'sv2013')
    output['conf_style_id'] = kwargs.get('conf_style', output['conf_id'])
    output['navmenu'] = output['conf_style_id'] + '/templates/navmenu.html'
    output['sponsors'] = output['conf_style_id'] + '/templates/sponsors.html'
    output['head'] = output['conf_style_id'] + '/templates/header.html'
    output['header'] = output['conf_style_id'] + '/templates/head.html'
    output['banner'] = output['conf_style_id'] + '/templates/banner.html'
    output['scripts'] = output['conf_style_id'] + '/templates/scripts.html'
    output['sponsors'] = output['conf_style_id'] + '/templates/sponsors.html'
    output['footer'] = output['conf_style_id'] + '/templates/footer.html'
    output['sidebar'] = output['conf_style_id'] + '/templates/sidebar.html'

    return output
