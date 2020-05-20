from django.urls import path


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('loeschen', views.loeschen, name='loeschen'),
    path('newtodo/', views.newtodo, name='newtodo'),
    path('newtodo/save', views.savenewtodo, name='savenewtodo'),
]
