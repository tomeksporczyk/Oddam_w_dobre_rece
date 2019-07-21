from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from OWDR.tokens import account_activation_token


def create_email_message(current_site, mail_subject, html_dir, user, to_email):
    '''
    :param current_site: get_current_site(request)
    :param mail_subject: str - email subject
    :param html_dir: str - dir of used html
    :param user: object user
    :return: EmailMessage(mail_subject, message, to)
    '''
    message = render_to_string(html_dir, {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
    })
    return EmailMessage(mail_subject, message, to=[to_email])