from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail
from pages.models import Page

def contact(request):
    pg=Page.objects.get(permalink='/contact')
    submitted=False
    if request.method=='POST':
        
        subject=request.POST['subject']
        yourname=request.POST['yourname']
        message=request.POST['message']
        email=request.POST['email']
        subject=yourname+ ' '+ subject
        send_mail(subject,message,'cromarties2913@gmail.com',[email])
        submitted=True
        context={
            'page_list':Page.objects.all(),
            'submitted':submitted
        }
        return render(request,'contacts/contact.html',context) 
    else:
        pass
    
    form=ContactForm()
    context={
        'form':form,
        'title':pg.title,
        'content':pg.bodytext,
        'last_updated':pg.update_date,
        'page_list':Page.objects.all(),
        'submitted':submitted,

    }    
    
    return render(request, 'contacts/contact.html',context)
    

