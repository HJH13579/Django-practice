from django.urls import path
from myapp import views

app_name='myapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('mon/', views.mon),
    path('tues/', views.tues),
    path('wends/', views.wends),
    path('hello/<str:name>/', views.hello),
    path('sum/<int:a>/<int:b>', views.sum_num),
]