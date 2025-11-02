from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_comment_notification(post, comment, request):
    if post.author.email and post.author != comment.author:
        subject = f'Новый комментарий к вашему посту "{post.title}"'
        html_message = render_to_string('emails/comment_notification.html', {
            'post': post,
            'comment': comment,
            'site_url': request.build_absolute_uri('/')[:-1]
        })
        plain_message = strip_tags(html_message)

        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[post.author.email],
            html_message=html_message,
        )


def send_welcome_email(user, request):
    subject = 'Добро пожаловать в Blogicum!'
    html_message = render_to_string('emails/welcome.html', {
        'user': user,
        'site_url': request.build_absolute_uri('/')[:-1]
    })
    plain_message = strip_tags(html_message)

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_message,
    )
