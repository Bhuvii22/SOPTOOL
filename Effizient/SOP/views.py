# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import SOPDocumentForm
def login(request):
    return render(request,'login.html')
def sopform(request):
    if request.method == 'POST':
        form = SOPDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'SOP Form Submission',
                'Thank you for submitting the SOP form. Here is your data:\n\n' + str(form.cleaned_data),
                'your-email@gmail.com',  # Replace with your email address
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('success')  # Redirect to a success page
    else:
        form = SOPDocumentForm()
    return render(request, 'sopform.html', {'form': form})

def success(request):
    return render(request, 'success.html')
