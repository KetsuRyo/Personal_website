from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .form import ContactForm  # 確保這個導入是正確的
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = "message" +" "+":"+" "+ form.cleaned_data['message'] +"\n"+ " "+ "from" +" "+":"+" "+ form.cleaned_data['email']
            send_mail(
                f'Message from {name} via Portfolio Website',
                message,
                'b01b01059@gmail.com',
                ['jackchunchiehliao@gmail.com'],
            )
            return redirect('contact')
        
    else:
        form = ContactForm()
    return render(request, 'base/home.html', {'form': form})