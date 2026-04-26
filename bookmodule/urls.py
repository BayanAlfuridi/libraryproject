from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/<int:val1>/', views.index2),
    path('', include('bookmodule.urls')),
]
