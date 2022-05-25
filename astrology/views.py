from sre_constants import IN
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'astrology/index.html')

def meetings(request):
    return render(request,'astrology/meetings.html')

def meeting_details(request):
    return render(request,'astrology/meeting-details.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        info = Info(name=name,email=email,subject=subject,message=message)
        info.save()

        send_mail(
           subject,
           f"{message} from {name}",
           f"{email}" ,
           ['funzoaid123@gmail.com'],
           fail_silently=False
        )
        return render(request,'astrology/contact.html',{
        "name":name,
    })

    return render(request,'astrology/contact.html',{
       
    })

def pujan_samagri (request):
    return render(request,"astrology/pujan_samagri.html")


