from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from book import views
from registration import views
from src import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls', namespace='books')),
    path('', include('registration.urls', namespace='registration'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)