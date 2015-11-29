from django.shortcuts import render
from django.core.mail import send_mail
from .forms import contactForm
from django.conf import settings

# Create your views here.

# if get authentication error, go to https://accounts.google.com/DisplayUnlockCaptcha
def contact(request):
    title = 'Context'
    form = contactForm(request.POST or None)
    confirm_message=None
    context = {'title':title, 'form':form}
    if form.is_valid():
        print(request.POST)
        print(form.cleaned_data['email'])
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        message = "%s %s" %(comment, name)
        #send_mail(name, message, emailFrom,emailTo, fail_silently=False)
        title="Done"
        confirm_message="confirm message"
        form = None
    context = {'title': title, 'form':form, 'confirm_message':confirm_message}

    #context = locals()
    template = 'contact.html'
    return render(request, template, context)