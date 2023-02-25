from django.urls import path

from . import views
from .views import index

app_name = 'musicapp'

urlpatterns = [

    path('', index, name='index'),
    path('music/<int:music_id>/', views.detail, name='detail'),
    path('add/', views.add_music, name='add_music'),
    path('update/<int:id>/',views.update,name='update'),
path('delete/<int:id>/',views.delete,name='delete')


]
