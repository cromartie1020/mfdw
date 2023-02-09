from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    if request.method=='POST':
        subject=request.POST['subject']
        yourname=request.POST['yourname']
        message=request.POST['messaage']
        email=request.POST['email']
        subject=yourname+ ' '+ subject
        send_mail(subject,message,'cromarties2913@gmail.com',[email])
        return redirect('home')
    else:
        form=ContactForm()

    context={
        'form':form
    }    

    return render(request, 'contacts/contact.html',context)
    

