
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('contact/',include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('',include ('pages.urls')),
   
    

    
]
handler404='pages.views.error_404_view' 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
