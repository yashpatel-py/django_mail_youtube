from django.shortcuts import render
from .forms import ContactUsForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def home(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # send_mail(subject, body, email, recipinet, fail_subject_trye)

            subject = "contact form Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email_id': form.cleaned_data['email_id'],
                'phone_number': form.cleaned_data['phone_number'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }

            message = '\n'.join(body.values())

            sender = form.cleaned_data['email_id']
            recipient = ['gameforyash@gmail.com']


            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)

            except BadHeaderError:
                return HttpResponse("Invalid hader found")

    context = {
        'form':form
    }

    return render(request, 'index.html', context)