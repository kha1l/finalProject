from django.urls import path
from .views import MainPage, UploadFile, SelectMySong, SelectSongs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPage.as_view(), name='head'),
    path('upload/', UploadFile.as_view(), name='upload'),
    path('music/', SelectMySong.as_view(), name='music'),
    path('search/', SelectSongs.as_view(), name='search')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
