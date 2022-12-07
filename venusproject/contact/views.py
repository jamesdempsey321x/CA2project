from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string('contact/emails/emails.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            })
            send_mail('The contact form subject', 'End', 'noreply@x00202628mytudublin.ie', ['X00202628@mytudublin.ie'], html_message=html)
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form 
    })