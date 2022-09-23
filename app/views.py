from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def index2(request, emails, message):
    send_mail(
        'This is a bot generated email',
        message,
        'noreply@buzzemail.com',
        emails,
        fail_silently=False,
    )
    return render(request, 'index.html', {})
