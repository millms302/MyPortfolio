from django.urls import path
from pages import views 

urlpatterns = [
    path('', views.about_me_view, name='about_me'),

]