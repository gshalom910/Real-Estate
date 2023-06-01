from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse



# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            subject= form.cleaned_data['subject']
            email= form.cleaned_data['email']
            message=form.cleaned_data['message']
            su=subject+' : '+first_name
            try:
                send_mail(su, message, email, ['admin@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("index")
    form = ContactForm()
    return render(request, "main/contact_us.html", {'form':form})