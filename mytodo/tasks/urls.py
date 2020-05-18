from django.urls import path


from . import views


urlpatterns = [
    path('newtodo/', views.newtodo, name='newtodo'),
    path('newtodo/save', views.savenewtodo, name='savenewtodo'),
]
