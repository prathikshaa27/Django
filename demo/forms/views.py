from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully")
    else:
        form = ContactForm()
    return render(request, 'forms/contact_form.html', {'form': form})
