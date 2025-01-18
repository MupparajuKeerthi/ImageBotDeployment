
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('user.urls')),
    path("",include('allauth.urls')),
    path('process/', views.process, name='process'),
    path('image-enhancement/', views.image_enhancement, name='image_enhancement'),
    path('image-captioning/', views.image_captioning, name='image_captioning'),
    path('similar-images/', views.similar_images, name='similar_images'),
    path('visual-qa/', views.visual_qa, name='visual_qa'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

