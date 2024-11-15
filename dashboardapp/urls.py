from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, test

urlpatterns = [
    # App Views
    path('', home, name='home'), 
    path('test', test, name="test"),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # If you have custom media paths like MEDIA_URL_DATA
    if hasattr(settings, 'MEDIA_URL_DATA') and hasattr(settings, 'MEDIA_ROOT_DATA'):
        urlpatterns += static(settings.MEDIA_URL_DATA, document_root=settings.MEDIA_ROOT_DATA)
