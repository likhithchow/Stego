from django.contrib import admin
from django.urls import path
from stegano_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('encryption/', views.encryption_view, name='encryption'),
    path('decryption/', views.decryption_view, name='decryption'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('download/<str:image_path>/', views.download_image, name='download_image'),
]

# Allow media access (only works on Render if file exists in /media)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
