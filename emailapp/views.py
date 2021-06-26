from django.shortcuts import render
from django.core.mail import EmailMessage
# Create your views here.

def app(request):
    # EmailMessage(subject,body,to)
    email = EmailMessage('Sub here','body here',to=['shreyas1427@gmail.com','ishank7057@gmail.com'])
    email.send()
    return render(request,'app.html')