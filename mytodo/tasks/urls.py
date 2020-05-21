from django.urls import path


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/bearbeiten', views.bearbeiten, name='bearbeiten'),
    path('<int:todo_id>/bearbeiten/save', views.save, name='save'),
    path('beispiel', views.beispiel, name='beispiel'),
    path('impressum', views.impressum, name='impressum'),
    path('loeschen', views.loeschen, name='loeschen'),
    path('newtodo/', views.newtodo, name='newtodo'),
    path('newtodo/save', views.savenewtodo, name='savenewtodo'),
]
