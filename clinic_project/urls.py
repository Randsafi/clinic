from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    context = {
        'username': request.user.username,
        'is_doctor': request.user.groups.filter(name='Doctors').exists()
    }
    return render(request, 'index.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('account/', include('accounts.urls')),
    path('', include('clinic.urls')),
    path('teste/', include('teste.urls')),
    path('question/', include('Question.urls')),
    path('api/', include('api_app.urls')),
] +static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)\
 +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
