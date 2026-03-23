from django.urls import path
from myapp import views
# myapp/urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),  # <--- เติม / ตรงนี้
]