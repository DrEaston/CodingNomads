from django.urls import path
from projects import views


app_name = 'projects'

urlpatterns = [
    path('<int:pk>', views.detail, name='detail'),
    path('', views.index, name='projects'),
]