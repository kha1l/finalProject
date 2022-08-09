from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
    path('account/', include('account.urls')),
    path('api/', include('api.urls'))
]
