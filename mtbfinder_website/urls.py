from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mtbfinder_website.apps.public.urls")),
    path("accounts/", include("mtbfinder_website.apps.accounts.urls")),
    path("contact/", include("mtbfinder_website.apps.contact.urls")),
    path("bikes/", include('bikes.urls', namespace='bikes')),
    path('webaccounts/', include("webaccounts.urls")),
    


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


