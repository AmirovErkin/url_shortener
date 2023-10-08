from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:shortened_url>/', views.redirect_to_original, name='redirect'),
]
