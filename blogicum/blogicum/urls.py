from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
    path('', include('pages.urls')),

    path('registration/', RegistrationView.as_view(), name='registration'),
    path('auth/registration/', RegistrationView.as_view(), name='auth_registration'),
]

handler404 = 'pages.views.page_not_found'
handler403 = 'pages.views.permission_denied'
handler500 = 'pages.views.server_error'
handler403csrf = 'pages.views.csrf_failure'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
