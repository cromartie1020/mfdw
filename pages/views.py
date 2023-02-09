from django.shortcuts import render,get_object_or_404 
from .models import Page
 

#def index(request):
#    return render(request, 'pages/page.html')


def index(request, pagename):
    pagename='/'+pagename

    print('pagename',pagename)
    pg=get_object_or_404(Page,permalink=pagename)
    context={
        'title':pg.title,
        'content':pg.bodytext,
        'last_updated':pg.update_date,
        'page_list':Page.objects.all(),
    }
    
    
    return render(request,'pages/page.html', context)

def error_404_view(request, exception):
    return render(request, 'pages/404.html',{})