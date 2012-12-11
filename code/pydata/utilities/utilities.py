from os import popen

MAIL = '/usr/sbin/sendmail'


def send_plain_email(recipient, message, sender='admin@pydata.org', subject='Automated Email from PyData.org'):
    template = """To: {0}
From: {1}
Subject: {2}

{3}

"""
    send_string = template.format(recipient, sender, subject, message)

    print send_string

    p = popen(MAIL + ' -t', 'w')
    p.write(send_string)
    exitcode = p.close()

    return exitcode

