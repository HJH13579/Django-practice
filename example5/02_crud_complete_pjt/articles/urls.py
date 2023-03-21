from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
