from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def project_view(request):
    return render(request, 'projects/projects.html')

def contact_view(request):
    if request.method == 'POST':
        # means the form has been submitted
        form = ContactForm(request.POST)
        # Collect the data from the form and validate it.
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
        
    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})