from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from mysite import settings
import smtplib


def sendmail(to, subject, text, attach=[], mtype='html'):
    ok = True
    # import ipdb; ipdb.set_trace()
    gmail_user = settings.EMAIL_HOST_USER
    gmail_pwd  = settings.EMAIL_HOST_PASSWORD

    msg = MIMEMultipart('alternative')

    msg['From']    = gmail_user
    msg['To']      = to
    msg['Cc']      = 'safiulla.sk@gmail.com'
    msg['Subject'] = subject

    msg.attach(MIMEText(text, mtype))

    for a in attach:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(a))
        msg.attach(part)

    try:
        mailServer = smtplib.SMTP("smtp.gmail.com", 687)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, [to, msg['Cc']], msg.as_string())
        mailServer.close()
    except:
        ok = False
    return ok