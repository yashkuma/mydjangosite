from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='add'),
    path('add',views.add,name='add')
]
