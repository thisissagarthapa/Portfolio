from django.shortcuts import render,redirect
from .models import Info
from .models import Project
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.http import HttpResponse, Http404
import os
import datetime

# Create your views here.
date1=datetime.datetime.now()
date = datetime.datetime.now().year
def index(request):
    data=Project.objects.all()
    print(data)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        emailsub=request.POST['emailsub']
        message=request.POST['message']
        info=Info(name=name,email=email,phoneno=phoneno,emailsub=emailsub,message=message)
        info.save()
           # Prepare email content
        context = {
            'name': name,
            'email': email,
            'phone': phoneno,
            'emailsub':emailsub,
            'message': message,
            'date1':date1,
        }        
        # Render HTML email content
        html_content = render_to_string('msg.html', context)
        
        # Create plain text version
        plain_content = strip_tags(html_content)

        # Create the email
        subject = "Thank You for Contacting Us!"
        from_email = 'kingstonboysagar@gmail.com'
        recipient_list = [email]

        # Use EmailMultiAlternatives to send multi-part email
        email = EmailMultiAlternatives(
            subject=subject,
            body=plain_content,  # The plain text part
            from_email=from_email,
            to=recipient_list,
        )

        # Attach HTML content
        email.attach_alternative(html_content, "text/html")

        # Send the email
        email.send(fail_silently=False)

        # Show a success message to the user
        messages.success(request, f"Hi {name}, thanks for contacting us! Please check your email for confirmation.")
        return redirect(index)
    
     
    return render(request,'portfolio.html',{'date':date,'data':data})

import os
from django.http import HttpResponse, Http404

def download_cv(request):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'main', 'static', 'files', 'Sagar.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename="Sagar.pdf"'
            return response
    else:
        raise Http404("File not found")


def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def projects(request):    
    data=Project.objects.all()  
    return render(request,'projects.html',{'date':date,'data':data})
def contact(request):
    return render(request,'contact.html')
