from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("user.urls", namespace='accounts')),
    path('accounts/', include("django.contrib.auth.urls")),
]
