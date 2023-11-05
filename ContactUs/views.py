from django.shortcuts import render, redirect

from ContactUs.forms import ContactUsForm


# Create your views here.

def ContactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomePage:home')
    else:
        form = ContactUsForm()
    return render(request, 'ContactUs/ContactUs.html', {'form': form})

